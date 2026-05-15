
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme
from .models import Character, Series
from .forms import SignUpForm, LoginForm
# Create your views here.

@login_required
def home(request):
    series = Series.objects.all()
    return render(request, 'home.html', {'series': series})

@login_required
def series_list(request):
    series = Series.objects.all()
    return render(request, 'series_list.html', {'series': series})

@login_required
def character_list(request):
    characters = Character.objects.all()
    return render(request, 'characters.html', {'characters': characters})

@login_required
def audiobooks(request):
    return render(request, 'audiobooks.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def black_sun_origins(request):
    return render(request, 'black_sun_origins.html')

@login_required
def sentinels(request):
    return render(request, 'sentinels.html')

@login_required
def cometson(request):
    return render(request, 'cometson.html')

@login_required
def paragons(request):
    return render(request, 'paragons.html')

@login_required
def order_of_the_abyss(request):
    return render(request, 'order-of-the-abyss.html')

@login_required
def independence_day(request):
    return render(request, 'independence-day.html')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    next_url = request.GET.get('next') or request.POST.get('next')
    if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        next_url = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(next_url or 'home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'next': next_url})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    next_url = request.GET.get('next') or request.POST.get('next')
    if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        next_url = None
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(next_url or 'home')
    else:
        form = LoginForm(request=request)
    return render(request, 'login.html', {'form': form, 'next': next_url})

def logout_view(request):
    logout(request)
    return redirect('home')