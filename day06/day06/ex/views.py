from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from random import choice
from .forms import RegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login


def index(request):
    if 'user' not in request.session or request.session.get_expiry_age() == 0:
        user = choice(settings.NAMES)
        request.session['user'] = user
        request.session.set_expiry(value=42)
        request.session.clear_expired()
    return render(request, 'ex/index.html', context={'user': request.session['user']})


class Login(LoginView):
    template_name = 'ex/login.html'
    success_url = reverse_lazy('home')


class Logout(LogoutView):
    next_page = 'home'


class Registration(CreateView):
    template_name = 'ex/registration.html'
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        return redirect(reverse_lazy('home'))
