from django import forms
from .models import SettingColorTable,SettingFontTable


class SettingColorForm(forms.ModelForm):
    # Define the color field with a dropdown populated by SettingColorTable
    color = forms.ModelChoiceField(
        queryset=SettingColorTable.objects.all(),
        widget=forms.Select(attrs={'id': 'id_card', 'class': 'form-select'}),
        empty_label="Select a color"
    )

    class Meta:
        model = SettingColorTable
        fields = ['color']

    
class SettingFontForm(forms.ModelForm):
    # Define the font field with a dropdown populated by SettingFontrTable
    font = forms.ModelChoiceField(
        queryset=SettingFontTable.objects.all(),
        widget=forms.Select(attrs={'id': 'id_card', 'class': 'form-select'}),
        empty_label="Select a Font"
    )

    class Meta:
        model = SettingFontTable
        fields = ['font']