from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    username.widget.attrs.update({'class': 'input-block-level', 'placeholder': 'Username'})
    password.widget.attrs.update({'class': 'input-block-level', 'placeholder': 'Password'})


@login_required(login_url='/account/login/')
def index(request):
    return render(request, 'account/index.html')


#def change_password(request):
    #u = User.objects.get(username__exact='john')
    #u.set_password('new password')
    #u.save()


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
                #return HttpResponseRedirect(reverse(account.views.index))
            else:
                errors.append("Disabled account")
        else:
            errors.append("Invalid login")

    return render(request, 'account/login.html', {
        'errors': errors,
        'form': form,
    })


# TODO: Finish
def logout_view(request):
    logout(request)
    return redirect(reverse('podr:index'))


#def register(request):
    #if valid input and user doesn't exist
        #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

        # At this point, user is a User object that has already been saved
        # to the database. You can continue to change its attributes
        # if you want to change other fields.
        #user.save()
    #else show form
