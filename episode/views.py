from django.shortcuts import render, get_object_or_404
from podr.models import Episode


def index(request):
    latest_episode_list = Episode.objects.order_by('-title')#[:5]
    context = {
        'latest_episode_list': latest_episode_list,
    }
    return render(request, 'episode/index.html', context)


def details(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    return render(request, 'episode/details.html', {'episode': episode})