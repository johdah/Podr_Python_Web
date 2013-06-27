from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

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
def add(request):
    podcast, created = Podcast.objects.get_or_create(link=request.POST['link'], defaults={'link': request.POST['link']})

    podcast = iTunesFeed.iTunesFeedParser.parseChannel(podcast)
    podcast.save()

    return HttpResponseRedirect('/podcast/%i/' % podcast.id)


def details(request, podcast_id):
    podcast = get_object_or_404(Podcast, pk=podcast_id)
    return render(request, 'podcast/details.html', {'podcast': podcast})


## Todo: Add a check so that we only allow an update every 15 minutes
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

    return HttpResponseRedirect('/podcast/%i/' % podcast.id)