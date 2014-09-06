from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from .models import Channel, User


def index(request):
    """
    Index view.
    """
    context = {"channels": Channel.objects.all()}
    return render_to_response('chat/index.html', context, context_instance=RequestContext(request))


def channel(request, slug):
    """
    Show a channel.
    """
    context = {
        "channel": get_object_or_404(Channel, slug=slug),
        "channels": Channel.objects.all()
    }
    return render_to_response("chat/channel.html", context, context_instance=RequestContext(request))


def create_channel(request):
    """
    Handles post from the "Create a channel" form on the homepage, and
    redirects to the new channel.
    """
    name = request.POST.get("name")
    if name:
        channel, created = Channel.objects.get_or_create(name=name)
        return redirect(channel)
    return redirect(index)
