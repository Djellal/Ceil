from django.contrib import admin
from .models import Session, Profession, CourseType, Course

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

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'fee_value')
    search_fields = ('name', 'name_ar')
    
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

class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_ar')
    search_fields = ('name', 'name_ar')
    
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

class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'course_type', 'duration', 'is_active')
    search_fields = ('code', 'name', 'name_ar')
    list_filter = ('course_type', 'is_active')
    
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
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(CourseType, CourseTypeAdmin)
admin.site.register(Course, CourseAdmin)
