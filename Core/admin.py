from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Session

class SessionAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'start_date', 'end_date')
    search_fields = ('code', 'name', 'name_ar')
    list_filter = ('start_date', 'end_date')

    def has_module_permission(self, request):
        return request.user.groups.filter(name='Admin').exists()

    def has_view_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists()

    def has_add_permission(self, request):
        return request.user.groups.filter(name='Admin').exists()

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists()

admin.site.register(Session, SessionAdmin)
