from django import forms
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from podr.models import Podcast, UserPodcast, UserEpisode
from podr.utils import iTunesFeed


class AddPodcastForm(forms.Form):
    link = forms.CharField(max_length=255)


def index(request):
    latest_podcast_list = Podcast.objects.order_by('-title')[:5]
    context = {
        'latest_podcast_list': latest_podcast_list,
        'form': AddPodcastForm()
    }
    return render(request, 'podcast/index.html', context)


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
    is_following = UserPodcast.objects.filter(podcast=podcast_id, user=request.user.id).exists()

    return render(request, 'podcast/details.html', {'podcast': podcast, 'is_following': is_following})


@login_required(login_url='/account/login/')
def follow(request, podcast_id):
    podcast = get_object_or_404(Podcast, pk=podcast_id)
    userPodcast = UserPodcast.objects.get_or_create(podcast=podcast, user=request.user)

    return redirect(reverse('podcast:details', kwargs={'podcast_id': podcast_id}))


@login_required(login_url='/account/login/')
def unfollow(request, podcast_id):
    podcast = get_object_or_404(Podcast, pk=podcast_id)
    userPodcast = get_object_or_404(UserPodcast, podcast=podcast, user=request.user)
    userPodcast.delete()

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
            userEpisode = UserEpisode(episode=episode, user=userPodcast.user)
            userEpisode.save()

    return redirect(reverse('podcast:details', kwargs={'podcast_id': podcast_id}))