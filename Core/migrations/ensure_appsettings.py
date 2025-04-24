from django.db import migrations

def create_default_appsettings(apps, schema_editor):
    AppSettings = apps.get_model('Core', 'AppSettings')
    if not AppSettings.objects.exists():
        AppSettings.objects.create(
            organization_name='Ceilgest',
            # Default values for other fields will be used
        )

def reverse_default_appsettings(apps, schema_editor):
    # This migration is safe to reverse
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('Core', '0002_appsettings'),  # Update this to match your latest migration
    ]

    operations = [
        migrations.RunPython(create_default_appsettings, reverse_default_appsettings),
    ]