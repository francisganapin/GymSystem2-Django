from .models import SettingColorTable


def background_color_context(request):
    active_setting = SettingColorTable.objects.filter(active=1).first()
    background_color = active_setting.value if active_setting else '#FFFFFF'
    return {
        'background_color': background_color
    }
