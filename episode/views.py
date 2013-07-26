from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from podr.models import Episode, UserEpisode, UserPodcast


@login_required(login_url='/account/login/')
def index(request):
    latest_user_episode_list = UserEpisode.objects.filter(user=request.user.id, archived=False).order_by("-episode__pub_date")

    paginator = Paginator(latest_user_episode_list, 50) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        episodes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        episodes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        episodes = paginator.page(paginator.num_pages)

    context = {
        'episodes': episodes,
    }
    return render(request, 'episode/index.html', context)


def details(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    userEpisode, created = UserEpisode.objects.get_or_create(episode=episode, user=request.user.id).first()
    userPodcast, created = UserPodcast.objects.get_or_create(podcast=episode.podcast, user=request.user.id)

    context = {
        'episode': episode,
        'userepisode': userEpisode,
        'userpodcast': userPodcast,
    }
    return render(request, 'episode/details.html', context)


@login_required(login_url='/account/login/')
def archive(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    userEpisode = get_object_or_404(UserEpisode, episode=episode, user=request.user)
    userEpisode.archived = True
    userEpisode.save()

    return redirect(reverse('episode:details', kwargs={'episode_id': episode_id}))


@login_required(login_url='/account/login/')
def star(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    userEpisode, created = UserEpisode.objects.get_or_create(episode=episode, user=request.user)
    userEpisode.starred = True
    userEpisode.save()

    return redirect(reverse('episode:details', kwargs={'episode_id': episode_id}))


@login_required(login_url='/account/login/')
def starred(request):
    starred_user_episode_list = UserEpisode.objects.filter(user=request.user.id, starred=True).order_by("-episode__pub_date")

    paginator = Paginator(starred_user_episode_list, 50) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        episodes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        episodes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        episodes = paginator.page(paginator.num_pages)

    context = {
        'episodes': episodes,
        }
    return render(request, 'episode/starred.html', context)


@login_required(login_url='/account/login/')
def thumb_down(request, episode_id):
    userEpisode, created = UserEpisode.objects.get_or_create(episode=episode_id, user=request.user)
    userEpisode.rating = -1
    userEpisode.save()

    return redirect(reverse('episode:details', kwargs={'episode_id': episode_id}))


@login_required(login_url='/account/login/')
def thumb_up(request, episode_id):
    userEpisode, created = UserEpisode.objects.get_or_create(episode=episode_id, user=request.user)
    userEpisode.rating = 1
    userEpisode.save()

    return redirect(reverse('episode:details', kwargs={'episode_id': episode_id}))


@login_required(login_url='/account/login/')
def unarchive(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    userEpisode, created = UserEpisode.objects.get_or_create(episode=episode, user=request.user)
    userEpisode.archived = False
    userEpisode.save()

    return redirect(reverse('episode:details', kwargs={'episode_id': episode_id}))


@login_required(login_url='/account/login/')
def unstar(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    userEpisode, created = UserEpisode.objects.get_or_create(episode=episode, user=request.user)
    userEpisode.starred = False
    userEpisode.save()

    return redirect(reverse('episode:details', kwargs={'episode_id': episode_id}))