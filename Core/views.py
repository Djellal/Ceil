from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .models import Session, AppSettings, State, Municipality, Profession, CourseType, Course
from .forms import SessionForm, AppSettingsForm, StateForm, MunicipalityForm, ProfessionForm, CourseTypeForm, CourseForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='Admin').exists()

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
    """
    View for the home page
    """
    return render(request, 'Core/home.html')

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
        form = AppSettingsForm(request.POST, request.FILES, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, 'Settings updated successfully.')
            return redirect('app_settings_edit')
    else:
        form = AppSettingsForm(instance=settings)
    
    return render(request, 'Core/app_settings_form.html', {'form': form})


# State CRUD views
@user_passes_test(is_admin)
def state_list(request):
    states = State.objects.all().order_by('name')
    return render(request, 'Core/state_list.html', {'states': states})

@user_passes_test(is_admin)
def state_create(request):
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'State created successfully.')
            return redirect('state_list')
    else:
        form = StateForm()
    
    return render(request, 'Core/state_form.html', {'form': form, 'title': 'Create State'})

@user_passes_test(is_admin)
def state_update(request, pk):
    state = get_object_or_404(State, pk=pk)
    
    if request.method == 'POST':
        form = StateForm(request.POST, instance=state)
        if form.is_valid():
            form.save()
            messages.success(request, 'State updated successfully.')
            return redirect('state_list')
    else:
        form = StateForm(instance=state)
    
    return render(request, 'Core/state_form.html', {'form': form, 'title': 'Update State'})

@user_passes_test(is_admin)
def state_delete(request, pk):
    state = get_object_or_404(State, pk=pk)
    
    if request.method == 'POST':
        state.delete()
        messages.success(request, 'State deleted successfully.')
        return redirect('state_list')
    
    return render(request, 'Core/state_confirm_delete.html', {'state': state})

@user_passes_test(is_admin)
def state_detail(request, pk):
    state = get_object_or_404(State, pk=pk)
    municipalities = state.municipalities.all().order_by('name')
    
    # Handle municipality creation
    if request.method == 'POST':
        form = MunicipalityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Municipality added successfully.')
            return redirect('state_detail', pk=state.pk)
    else:
        form = MunicipalityForm(initial={'state': state})
    
    return render(request, 'Core/state_detail.html', {
        'state': state, 
        'municipalities': municipalities,
        'form': form
    })

# Municipality CRUD views (within state context)
@user_passes_test(is_admin)
def municipality_update(request, state_pk, pk):
    state = get_object_or_404(State, pk=state_pk)
    municipality = get_object_or_404(Municipality, pk=pk, state=state)
    
    if request.method == 'POST':
        form = MunicipalityForm(request.POST, instance=municipality)
        if form.is_valid():
            form.save()
            messages.success(request, 'Municipality updated successfully.')
            return redirect('state_detail', pk=state.pk)
    else:
        form = MunicipalityForm(instance=municipality)
    
    return render(request, 'Core/municipality_form.html', {
        'form': form, 
        'state': state,
        'municipality': municipality,
        'title': 'Update Municipality'
    })

@user_passes_test(is_admin)
def municipality_delete(request, state_pk, pk):
    state = get_object_or_404(State, pk=state_pk)
    municipality = get_object_or_404(Municipality, pk=pk, state=state)
    
    if request.method == 'POST':
        municipality.delete()
        messages.success(request, 'Municipality deleted successfully.')
        return redirect('state_detail', pk=state.pk)
    
    return render(request, 'Core/municipality_confirm_delete.html', {
        'state': state,
        'municipality': municipality
    })

# Profession CRUD views
@user_passes_test(is_admin)
def profession_list(request):
    professions = Profession.objects.all().order_by('name')
    return render(request, 'Core/profession_list.html', {'professions': professions})

@user_passes_test(is_admin)
def profession_create(request):
    if request.method == 'POST':
        form = ProfessionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profession created successfully.')
            return redirect('profession_list')
    else:
        form = ProfessionForm()
    
    return render(request, 'Core/profession_form.html', {'form': form, 'title': 'Create Profession'})

@user_passes_test(is_admin)
def profession_update(request, pk):
    profession = get_object_or_404(Profession, pk=pk)
    
    if request.method == 'POST':
        form = ProfessionForm(request.POST, instance=profession)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profession updated successfully.')
            return redirect('profession_list')
    else:
        form = ProfessionForm(instance=profession)
    
    return render(request, 'Core/profession_form.html', {'form': form, 'title': 'Update Profession'})

@user_passes_test(is_admin)
def profession_delete(request, pk):
    profession = get_object_or_404(Profession, pk=pk)
    
    if request.method == 'POST':
        profession.delete()
        messages.success(request, 'Profession deleted successfully.')
        return redirect('profession_list')
    
    return render(request, 'Core/profession_confirm_delete.html', {'profession': profession})

# CourseType CRUD views
@user_passes_test(is_admin)
def course_type_list(request):
    course_types = CourseType.objects.all().order_by('name')
    return render(request, 'Core/course_type_list.html', {'course_types': course_types})

@user_passes_test(is_admin)
def course_type_create(request):
    if request.method == 'POST':
        form = CourseTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Type created successfully.')
            return redirect('course_type_list')
    else:
        form = CourseTypeForm()
    
    return render(request, 'Core/course_type_form.html', {'form': form, 'title': 'Create Course Type'})

@user_passes_test(is_admin)
def course_type_update(request, pk):
    course_type = get_object_or_404(CourseType, pk=pk)
    
    if request.method == 'POST':
        form = CourseTypeForm(request.POST, instance=course_type)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Type updated successfully.')
            return redirect('course_type_list')
    else:
        form = CourseTypeForm(instance=course_type)
    
    return render(request, 'Core/course_type_form.html', {'form': form, 'title': 'Update Course Type'})

@user_passes_test(is_admin)
def course_type_delete(request, pk):
    course_type = get_object_or_404(CourseType, pk=pk)
    
    if request.method == 'POST':
        course_type.delete()
        messages.success(request, 'Course Type deleted successfully.')
        return redirect('course_type_list')
    
    return render(request, 'Core/course_type_confirm_delete.html', {'course_type': course_type})

# Course CRUD views
@user_passes_test(is_admin)
def course_list(request):
    courses = Course.objects.all().order_by('code')
    return render(request, 'Core/course_list.html', {'courses': courses})

@user_passes_test(is_admin)
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course created successfully.')
            return redirect('course_list')
    else:
        form = CourseForm()
    
    return render(request, 'Core/course_form.html', {'form': form, 'title': 'Create Course'})

@user_passes_test(is_admin)
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully.')
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    
    return render(request, 'Core/course_form.html', {'form': form, 'title': 'Update Course'})

@user_passes_test(is_admin)
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course deleted successfully.')
        return redirect('course_list')
    
    return render(request, 'Core/course_confirm_delete.html', {'course': course})

@user_passes_test(is_admin)
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    return render(request, 'Core/course_detail.html', {'course': course})
