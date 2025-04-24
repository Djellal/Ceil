from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.home_view, name='profile_redirect'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Updated logout path
    path('sessions/', views.session_list, name='session_list'),
    path('sessions/create/', views.session_create, name='session_create'),
    path('sessions/<int:pk>/update/', views.session_update, name='session_update'),
    path('sessions/<int:pk>/delete/', views.session_delete, name='session_delete'),
    path('settings/', views.app_settings_edit, name='app_settings_edit'),
]