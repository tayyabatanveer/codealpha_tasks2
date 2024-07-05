from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Registration
from .forms import EventRegistrationForm

def landing_page(request):
    return render(request, 'landing_page.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('event_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.info(request, f'You are now logged in as {user.username}.')
            return redirect('event_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    auth_logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('landing_page')

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_detail.html', {'event': event})

@login_required
def event_register(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.user = request.user
            registration.save()
            messages.success(request, f'You have successfully registered for {event.title}.')
            return redirect('event_list')
    else:
        form = EventRegistrationForm()
    return render(request, 'event_register.html', {'form': form, 'event': event})

@login_required
def my_registrations(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'my_registrations.html', {'registrations': registrations})

@login_required
def event_unregister(request, registration_id):
    registration = get_object_or_404(Registration, id=registration_id, user=request.user)
    if request.method == 'POST':
        registration.delete()
        messages.success(request, 'You have successfully unregistered from the event.')
        return redirect('my_registrations')
    return redirect('event_list')
