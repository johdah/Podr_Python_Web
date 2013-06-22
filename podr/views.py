from django.shortcuts import render


def index(request):
    context = {'title': 'Welcome to PodR'}
    return render(request, 'podr/index.html', context)