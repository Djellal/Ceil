from .models import AppSettings

def app_settings(request):
    """
    Adds app_settings to the context of all templates.
    """
    return {
        'app_settings': AppSettings.get_settings(),
    }