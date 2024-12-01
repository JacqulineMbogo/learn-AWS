from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm, UpdateUserForm, UpdateProfileForm

from .models import Profile
from django.contrib.auth.models import auth

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            current_user = form.save(commit=False)

            form.save()

            profile = Profile.objects.create(user=current_user)
            return redirect("login")

    context = {'form': form}

    return render(request, 'register.html', context=context)


def login(request):
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {'form': form}

    return render(request, 'login.html', context=context)


def logout(request):
    auth.logout(request)
    redirect("")


@login_required(login_url='login')
def profile(request):
    user_form = UpdateUserForm(instance=request.user)

    profile = Profile.objects.get(user=request.user)

    profile_form = UpdateProfileForm(instance=profile)

    if request.method == 'POST':

        user_form = UpdateUserForm(request.POST, instance=request.user)

        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid():
            user_form.save()

            return redirect("dashboard")

        if profile_form.is_valid():
            profile_form.save()

            return redirect("dashboard")

    context = {'user_form': user_form, 'profile_form': profile_form}

    return render(request, 'profile.html', context=context)


@login_required(login_url='login')
def delete(request):
    if request.method == "POST":
        deleteUser = User.objects.get(username=request.user)

        deleteUser.delete()

        return redirect("")

    return render(request, 'delete.html')


@login_required(login_url='login')
def dashboard(request):
    profile_pic = Profile.objects.get(user=request.user)

    context = {'profilePic': profile_pic}

    return render(request, 'dashboard.html', context=context)

