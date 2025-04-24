from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Session, AppSettings
from .forms import SessionForm, AppSettingsForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@user_passes_test(is_admin)
def session_list(request):
    sessions = Session.objects.all()
    return render(request, 'Core/session_list.html', {'sessions': sessions})

@user_passes_test(is_admin)
def session_create(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('session_list')
    else:
        form = SessionForm()
    return render(request, 'Core/session_form.html', {'form': form})

@user_passes_test(is_admin)
def session_update(request, pk):
    session = get_object_or_404(Session, pk=pk)
    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('session_list')
    else:
        form = SessionForm(instance=session)
    return render(request, 'Core/session_form.html', {'form': form})

@user_passes_test(is_admin)
def session_delete(request, pk):
    session = get_object_or_404(Session, pk=pk)
    if request.method == 'POST':
        session.delete()
        return redirect('session_list')
    return render(request, 'Core/session_confirm_delete.html', {'session': session})


@login_required
def home_view(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# In any view where you need the settings
from .models import AppSettings

def some_view(request):
    settings = AppSettings.get_settings()
    # Use settings...

@user_passes_test(is_admin)
def app_settings_edit(request):
    # Get the singleton instance or create it if it doesn't exist
    settings, created = AppSettings.objects.get_or_create(pk=1)
    
    if request.method == 'POST':
        form = AppSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            return redirect('app_settings_edit')
    else:
        form = AppSettingsForm(instance=settings)
    
    return render(request, 'Core/app_settings_form.html', {'form': form})
