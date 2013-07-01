from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from podr.models import Episode, UserEpisode, UserPodcast


@login_required(login_url='/account/login/')
def index(request):
    latest_user_episode_list = UserEpisode.objects.filter(user=request.user.id, archived=False).order_by("-episode__pub_date")
    context = {
        'latest_user_episode_list': latest_user_episode_list,
    }
    return render(request, 'episode/index.html', context)


def details(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    userEpisode = UserEpisode.objects.filter(episode=episode, user=request.user.id).first()
    is_following_podcast = UserPodcast.objects.filter(podcast=episode.podcast, user=request.user.id).exists()

    return render(request, 'episode/details.html', {
        'episode': episode, 'user_episode': userEpisode, 'is_following_podcast': is_following_podcast})


@login_required(login_url='/account/login/')
def archive(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    userEpisode = get_object_or_404(UserEpisode, episode=episode, user=request.user)
    userEpisode.archived = True
    userEpisode.save()

    return redirect(reverse('episode:details', kwargs={'episode_id': episode_id}))


@login_required(login_url='/account/login/')
def unarchive(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    userEpisode, created = UserEpisode.objects.get_or_create(episode=episode, user=request.user)
    userEpisode.archived = False
    userEpisode.save()

    return redirect(reverse('episode:details', kwargs={'episode_id': episode_id}))