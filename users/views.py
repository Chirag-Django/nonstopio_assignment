from django.shortcuts import render,redirect
from .forms import UserForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction


@transaction.atomic
def register(request):
    button_name = 'Click Here to Register'
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            user.set_password(user.password)
            user.profile.age = profile_form.cleaned_data.get('age')
            user.profile.address = profile_form.cleaned_data.get('address')
            user.save()
            return redirect('users:login')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'button_name':button_name
            })

@login_required
@transaction.atomic
def update_profile(request):
    button_name = 'Update Profile'
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            user.set_password(user.password)
            user.profile.age = profile_form.cleaned_data.get('age')
            user.profile.address = profile_form.cleaned_data.get('address')
            user.save()
            return redirect('users:login')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'button_name':button_name
        })