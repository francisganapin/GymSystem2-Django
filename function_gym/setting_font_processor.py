from .models import SettingFontTable


def font_family_context(request):
    active_setting = SettingFontTable.objects.filter(active=1).first()
    font_setting = active_setting.value if active_setting else 'sans-serif'
    return {
        'font_setting': font_setting
    }
