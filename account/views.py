from datetime import datetime
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from podr.models import UserPodcast, UserEpisode, UserProfile, UserUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    username.widget.attrs.update({'class': 'input-block-level', 'placeholder': 'Username'})
    password.widget.attrs.update({'class': 'input-block-level', 'placeholder': 'Password'})


@login_required(login_url='/account/login/')
def index(request):
    context = {
        'episode_thumbs_down': UserEpisode.objects.filter(user=request.user, rating=-1).count(),
        'episode_thumbs_up': UserEpisode.objects.filter(user=request.user, rating=1).count(),
        'following_podcasts': UserPodcast.objects.filter(user=request.user).count(),
        'starred_episodes': UserEpisode.objects.filter(user=request.user, starred=True).count(),
        'podcast_thumbs_down': UserPodcast.objects.filter(user=request.user, rating=-1).count(),
        'podcast_thumbs_up': UserPodcast.objects.filter(user=request.user, rating=1).count(),
        'user_profile': UserProfile.objects.get_or_create(user=request.user),
    }
    return render(request, 'account/index.html', context)


#def change_password(request):
    #u = User.objects.get(username__exact='john')
    #u.set_password('new password')
    #u.save()


@login_required(login_url='/account/login/')
def follow(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    userUser, created = UserUser.objects.get_or_create(source=request.user, target=user)
    userUser.following = True
    userUser.last_updated = datetime.now()
    userUser.save()

    return redirect(reverse('account:user_profile', kwargs={'user_id': user_id}))


# TODO: Add view
def login_view(request):
    form = LoginForm()
    errors = []

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return redirect(reverse('account:index'))
            else:
                errors.append("Disabled account")
        else:
            errors.append("Invalid login")

    return render(request, 'account/login.html', {
        'errors': errors,
        'form': form,
    })


# TODO: Finish
@login_required(login_url='/account/login/')
def logout_view(request):
    logout(request)
    return redirect(reverse('podr:index'))


@login_required(login_url='/account/login/')
def unfollow(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    userUser, created = UserUser.objects.get_or_create(source=request.user, target=user)
    userUser.following = False
    userUser.last_updated = datetime.now()
    userUser.save()

    return redirect(reverse('account:user_profile', kwargs={'user_id': user_id}))


@login_required(login_url='/account/login/')
def user_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    userProfile, created = UserProfile.objects.get_or_create(user=user)

    if not userProfile.public_profile:
        return render(request, 'account/user_profile_private.html')

    context = {
        'episode_thumbs_down': UserEpisode.objects.filter(user=user, rating=-1).count(),
        'episode_thumbs_up': UserEpisode.objects.filter(user=user, rating=1).count(),
        'following_podcasts': UserPodcast.objects.filter(user=user).count(),
        'starred_episodes': UserEpisode.objects.filter(user=user, starred=True).count(),
        'podcast_thumbs_down': UserPodcast.objects.filter(user=user, rating=-1).count(),
        'podcast_thumbs_up': UserPodcast.objects.filter(user=user, rating=1).count(),
        'user_following': UserUser.objects.filter(source=request.user, target=user, following=True).exists(),
        'user_profile': userProfile,
    }
    return render(request, 'account/user_profile.html', context)


#def register(request):
    #if valid input and user doesn't exist
        #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

        # At this point, user is a User object that has already been saved
        # to the database. You can continue to change its attributes
        # if you want to change other fields.
        #user.save()
    #else show form
