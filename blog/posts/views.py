import logging

from django.http import HttpResponse
from django.shortcuts import render, redirect

from posts.forms import PostForm
from posts.models import Post

logger = logging.getLogger(__name__)


def post_list(request):
    posts = Post.objects.order_by("-id")
    return render(request, "posts/list.html", {"posts": posts})


def post_admin(request):
    if request.user.is_anonymous:
        return redirect("admin:index")
    posts = Post.objects.filter(author=request.user).order_by("-id")
    return render(request, "posts/admin.html", {"posts": posts})


def post_add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                Post.objects.create(author=request.user, **form.cleaned_data)
                return redirect("home")
        else:
            form = PostForm()
        return render(request, "posts/add.html", {"form": form})
    return HttpResponse("You don't authenticated!")


def post_view(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "posts/details.html", {"post": post})
