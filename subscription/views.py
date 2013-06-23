from django import forms
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from podr.models import Subscription
from podr.utils import iTunesFeed


class AddSubscriptionForm(forms.Form):
    link = forms.CharField(max_length=255)


def index(request):
    latest_subscription_list = Subscription.objects.order_by('-title')[:5]
    context = {
        'latest_subscription_list': latest_subscription_list,
        'form': AddSubscriptionForm()
    }
    return render(request, 'subscription/index.html', context)

#
# A simple function for adding a new subscription.
#  If subscription already exists, it's updated, otherwise created
#
def add(request):
    subscription, created = Subscription.objects.get_or_create(link=request.POST['link'], defaults={'link': request.POST['link']})

    subscription = iTunesFeed.iTunesFeedParser.parseSubscription(subscription)
    subscription.save()
    return HttpResponse("Response: %s" % subscription.link)


def details(request, subscription_id):
    subscription = get_object_or_404(Subscription, pk=subscription_id)
    return render(request, 'subscription/details.html', {'subscription': subscription})