from django.apps import AppConfig
from django.db.utils import ProgrammingError, OperationalError
from django.db import connection

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Core'

    def ready(self):
        try:
            # Check if auth_group table exists
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1 FROM auth_group LIMIT 1")
            # Only import and run create_groups if tables exist
            from Core.groups import create_groups
            create_groups()
        except (ProgrammingError, OperationalError):
            # Tables don't exist yet, skip group creation
            pass
