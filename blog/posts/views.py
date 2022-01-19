import logging

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.http import urlencode

from posts.models import Post

logger = logging.getLogger(__name__)


def posts_index(request):
    result = ""
    user = User.objects.get(username=request.GET.get("author", "manti"))
    author_name = request.GET.get("author", "manti")
    for x in Post.objects.filter(author__username=author_name).order_by("-id"):
        result += f"<div style='border: 1px solid black'>"
        result += f"<h1>{x.title} #{x.id}</h1>"
        result += f"<div>{x.text}</div>"
        result += f"</div>"
    return HttpResponse(result)

