import logging

from django.http import HttpResponse

from posts.models import Post

logger = logging.getLogger(__name__)


def posts_index(request):
    author_name = request.GET.get("author", "manti")
    posts = Post.objects.filter(author__username=author_name).order_by("-id")
    return HttpResponse(posts)

