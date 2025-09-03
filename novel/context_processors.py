from .models import SiteSetting

def site_settings(request):
    try:
        setting = SiteSetting.objects.first()
    except SiteSetting.DoesNotExist:
        setting = None
    return {"site_setting": setting}
