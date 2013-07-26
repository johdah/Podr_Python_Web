from datetime import datetime
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from podr.models import Podcast, UserPodcast, UserEpisode
from podr.utils import iTunesFeed


class AddPodcastForm(forms.Form):
    link = forms.CharField(max_length=255)


def index(request):
    #podcasts_following_list = Podcast.objects.filter.order_by('-title')[:5]
    podcasts_following_list = UserPodcast.objects.filter(user=request.user.id).order_by("-podcast__title")
    context = {
        'podcast_list': podcasts_following_list,
        'form': AddPodcastForm()
    }
    return render(request, 'podcast/index.html', context)


def all(request):
    all_podcasts_list = Podcast.objects.order_by('-title')[:5]
    context = {
        'podcast_list': all_podcasts_list,
        'form': AddPodcastForm()
    }
    return render(request, 'podcast/all.html', context)


#
# A simple function for adding a new subscription.
# If subscription already exists, it's updated, otherwise created
#
@login_required(login_url='/account/login/')
def add(request):
    podcast, created = Podcast.objects.get_or_create(link=request.POST['link'], defaults={'link': request.POST['link']})

    podcast = iTunesFeed.iTunesFeedParser.parseChannel(podcast)
    podcast.save()

    return redirect(reverse('podcast:details', kwargs={'podcast_id': podcast.id}))


def details(request, podcast_id):
    podcast = get_object_or_404(Podcast, pk=podcast_id)
    userpodcast = UserPodcast.objects.filter(podcast=podcast_id, user=request.user.id)
    is_following = userpodcast.first() and userpodcast.first().following

    paginator = Paginator(podcast.sorted_episode_set, 50) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        episodes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        episodes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        episodes = paginator.page(paginator.num_pages)

    return render(request, 'podcast/details.html', {'podcast': podcast, 'is_following': is_following, 'episodes': episodes})


@login_required(login_url='/account/login/')
def follow(request, podcast_id):
    podcast = get_object_or_404(Podcast, pk=podcast_id)
    userPodcast, created = UserPodcast.objects.get_or_create(podcast=podcast, user=request.user)
    userPodcast.following = True
    userPodcast.last_updated = datetime.now()
    userPodcast.save()

    return redirect(reverse('podcast:details', kwargs={'podcast_id': podcast_id}))


@login_required(login_url='/account/login/')
def thumb_down(request, podcast_id):
    userPodcast, created = UserPodcast.objects.get_or_create(podcast=podcast_id, user=request.user)
    userPodcast.rating = -1
    userPodcast.save()

    return redirect(reverse('podcast:details', kwargs={'podcast_id': podcast_id}))


@login_required(login_url='/account/login/')
def thumb_up(request, podcast_id):
    userPodcast, created = UserPodcast.objects.get_or_create(podcast=podcast_id, user=request.user)
    userPodcast.rating = 1
    userPodcast.save()

    return redirect(reverse('podcast:details', kwargs={'podcast_id': podcast_id}))


@login_required(login_url='/account/login/')
def unfollow(request, podcast_id):
    podcast = get_object_or_404(Podcast, pk=podcast_id)
    userPodcast, created = UserPodcast.objects.get_or_create(podcast=podcast, user=request.user)
    userPodcast.following = False
    userPodcast.last_updated = datetime.now()
    userPodcast.save()

    return redirect(reverse('podcast:details', kwargs={'podcast_id': podcast_id}))


## Todo: Add a check so that we only allow an update every 15 minutes
@login_required(login_url='/account/login/')
def update(request, podcast_id):
    podcast = get_object_or_404(Podcast, pk=podcast_id)
    podcast, episodes = iTunesFeed.iTunesFeedParser.parse(podcast)
    podcast.save()

    userPodcasts = UserPodcast.objects.all().filter(podcast=podcast_id)

    for episode in episodes:
        episode.save()
        for userPodcast in userPodcasts:
            if userPodcast.following is True:
                userEpisode = UserEpisode(episode=episode, user=userPodcast.user)
                userEpisode.save()

    return redirect(reverse('podcast:details', kwargs={'podcast_id': podcast_id}))