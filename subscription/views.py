from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from podr.models import Subscription

def index(request):
    latest_subscription_list = Subscription.objects.order_by('-title')[:5]
    context = {'latest_subscription_list': latest_subscription_list}
    return render(request, 'subscription/index.html', context)

def add(request, link):
    return HttpResponse("You're adding subscription %s." % link)

def details(request, subscription_id):
    subscription = get_object_or_404(Subscription, pk=subscription_id)
    return render(request, 'subscription/details.html', {'subscription': subscription})