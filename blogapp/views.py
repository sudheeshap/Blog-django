from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.
from blogapp.models import *

def home_page(request):
    posts = Post.objects.all().order_by("-pub_date")
    paginator = Paginator(posts, 3)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("list.html", dict(posts=posts, user=request.user))
