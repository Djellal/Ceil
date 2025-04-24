from django.contrib.auth.models import Group

GROUPS = ['Admin', 'Teacher', 'Student']

def create_groups():
    for group_name in GROUPS:
        Group.objects.get_or_create(name=group_name)