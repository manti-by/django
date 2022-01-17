import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def profiles_index(request):
    # Processing GET params
    value = request.GET.get("get-key-1")
    value and logger.info(f"get-key-1 = {value}")
    value = request.GET.get("get-key-2")
    value and logger.info(f"get-key-2 = {value}")
    value = request.GET.get("get-key-3")
    value and logger.info(f"get-key-3 = {value}")

    # Processing POST params
    value = request.POST.get("post-key-1")
    value and logger.info(f"post-key-1 = {value}")
    value = request.POST.get("post-key-2")
    value and logger.info(f"post-key-2 = {value}")
    value = request.POST.get("post-key-3")
    value and logger.info(f"post-key-3 = {value}")

    return HttpResponse("Profiles index view")
