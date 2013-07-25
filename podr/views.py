from django.shortcuts import render


def index(request):
    context = {'title': 'Welcome to PodR'}
    return render(request, 'podr/index.html', context)


def about_changelog(request):
    context = {}
    return render(request, 'podr/about_changelog.html', context)