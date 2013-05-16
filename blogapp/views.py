from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.template import RequestContext
# Create your views here.
from blogapp.models import *

from django.forms import ModelForm

def home_page(request):
    user = get_object_or_404(User, username=request.user.username)
    posts = Post.objects.filter(user=user).order_by("-pub_date")
    paginator = Paginator(posts, 3)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1
    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)
    return render_to_response("list.html", {'posts': posts, 'user': request.user})

def detail(request, slug):
    item = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=item)
    templ = {'post': item, 'comments': comments, 'user': request.user }
    return render_to_response("detail.html", templ, context_instance=RequestContext(request))

def add_comment(request, pk):
    pst = request.POST
    if pst["author"]: 
        author = pst["author"]
    else:
        author = "Anonymous" 
    post=Post.objects.get(pk=pk)
    comment = Comment(post=post, author=author, body=pst["cm_body"])
    print comment.post
    comment.save()
    comments = Comment.objects.filter(post=post)
    return render_to_response("detail.html", {'user': request.user,'comments': comments, 'post': post })

#TODO
#def signup(request):
    #return render_to_response("signup.html", {'user': request.user})
    












"""
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]


def post(request, pk):
    print "Heyyy"
    post = Post.objects.get(pk=int(pk))
    comments = Comment.objects.filter(post=post)
    d = dict(post=post, comments=comments, form=CommentForm(), user=request.user)
    d.update(csrf(request))
    return render_to_response("post.html", d)
"""



"""def post(request, pk):
   
    post = Post.objects.get(pk=int(pk))
    d = dict(post=post, user=request.user)
    return render_to_response("post.html", d)
"""
"""
def add_comment(request, pk):
   
    p = request.POST

    if p.has_key("body") and p["body"]:
        author = "Anonymous"
        if p["author"]: author = p["author"]

        comment = Comment(post=Post.objects.get(pk=pk))
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False

        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect(reverse("blogapp.views.post", args=[pk]))

"""
