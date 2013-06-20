from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the podr index.")

def subscription(request):
    return HttpResponse("Hello, world. You're at the subscription index.")

def subscription_add(request, link):
    return HttpResponse("You're adding subscription %s." % link)

def subscription_details(request, subscription_id):
    return HttpResponse("You're looking at subscription %s." % subscription_id)