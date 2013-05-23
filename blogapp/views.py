from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from blogapp.myforms import PostForm, CommentForm
from blogapp.models import *

def home_page(request):
    usr = request.user
    if request.method == 'GET':
        if not usr.is_authenticated():
            return render_to_response("login.html")
        else: 
            user = get_object_or_404(User, username=usr.username)
            posts = Post.objects.filter(user=user).order_by("-pub_date")
            paginator = Paginator(posts, 3)
            try: page = int(request.GET.get("page", '1'))
            except ValueError: page = 1
            try:
                posts = paginator.page(page)
            except (InvalidPage, EmptyPage):
                posts = paginator.page(paginator.num_pages)
            return render_to_response("list.html", {'posts': posts, 'user': usr})  

def detail(request, slug):
    item = get_object_or_404(Post, slug=slug)
    cf = CommentForm()
    comments = Comment.objects.filter(post=item)
    return render_to_response("detail.html", {'post': item, 'comments': comments, 'user': request.user, 'form': cf})

def add_comment(request, pk):
    pst = request.POST
    if pst["author"]: 
        author = pst["author"]
    else:
        author = "Anonymous" 
    post=Post.objects.get(pk=pk)
    slug = post.slug
    comment = Comment(post=post, author=author, body=pst["body"])
    comment.save()
    return HttpResponseRedirect("/posts/" + slug)

def create_user(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        uname = form.cleaned_data['username']
        pwd = form.cleaned_data['password1']
        user = User.objects.create_user(uname, None, pwd)
        user.is_staff = True
        user.save()
        usr = authenticate(username=uname, password=pwd)
        if usr is not None:
            if usr.is_active:
                login(request, usr)
                return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')
    else:
        return render_to_response("register.html", {'form': form})
    
def check_user(request):
    username = request.POST['username']
    password = request.POST['password']
    if not username or not password:
        return render_to_response("login.html", {'error_msg': "Username and password are required!"})
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            print "# Return a 'disabled account' error message"
    else:
        return render_to_response("login.html", {'error_msg': "Invalid user"})
    return HttpResponseRedirect('/')

def add_post(request):
    pst = request.POST
    pf = PostForm(pst)  
    if request.method == 'POST':
        if pf.is_valid():
            title = pst['title']
            body = pst['body']
            slug = slugify(pst['title'])
            post = Post(title=title, body=body,slug=slug, user=request.user)
            post.save()
            return HttpResponseRedirect('/')
        return render_to_response("add_post.html", {'form': pf})    
    else:  
        return render_to_response("add_post.html", {'form': pf}) 
   


