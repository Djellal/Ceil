from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Add this line for the home page
    path('', views.home_view, name='home'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.home_view, name='profile_redirect'),
    # Add this line for the registration view
    path('accounts/register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Updated logout path
    path('sessions/', views.session_list, name='session_list'),
    path('sessions/create/', views.session_create, name='session_create'),
    path('sessions/<int:pk>/update/', views.session_update, name='session_update'),
    path('sessions/<int:pk>/delete/', views.session_delete, name='session_delete'),
    path('settings/', views.app_settings_edit, name='app_settings_edit'),
    
    # State URLs
    path('states/', views.state_list, name='state_list'),
    path('states/create/', views.state_create, name='state_create'),
    path('states/<int:pk>/', views.state_detail, name='state_detail'),
    path('states/<int:pk>/update/', views.state_update, name='state_update'),
    path('states/<int:pk>/delete/', views.state_delete, name='state_delete'),
    
    # Municipality URLs (nested under states)
    path('states/<int:state_pk>/municipalities/<int:pk>/update/', 
         views.municipality_update, name='municipality_update'),
    path('states/<int:state_pk>/municipalities/<int:pk>/delete/', 
         views.municipality_delete, name='municipality_delete'),
    
    # Profession URLs
    path('professions/', views.profession_list, name='profession_list'),
    path('professions/create/', views.profession_create, name='profession_create'),
    path('professions/<int:pk>/update/', views.profession_update, name='profession_update'),
    path('professions/<int:pk>/delete/', views.profession_delete, name='profession_delete'),
    
    # CourseType URLs
    path('course-types/', views.course_type_list, name='course_type_list'),
    path('course-types/create/', views.course_type_create, name='course_type_create'),
    path('course-types/<int:pk>/update/', views.course_type_update, name='course_type_update'),
    path('course-types/<int:pk>/delete/', views.course_type_delete, name='course_type_delete'),
    
    # Course URLs
    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/<int:pk>/update/', views.course_update, name='course_update'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),
]