from .models import AppSettings

def app_settings(request):
    """
    Adds app_settings to the context of all templates.
    """
    settings, created = AppSettings.objects.get_or_create(pk=1)
    return {
        'app_settings': settings,
    }