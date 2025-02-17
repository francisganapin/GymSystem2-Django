from django.shortcuts import render
from .models import SettingColorTable,SettingFontTable
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import SettingColorForm,SettingFontForm
from django.shortcuts import render,redirect

# Create your views here.
@login_required
def background_color_form_views(request):
    # Default background color
    selected_color = SettingColorTable.objects.filter(active=1).first()
    selected_font  = SettingFontTable.objects.filter(active=1).first()

    color_form = SettingColorForm(request.POST or None)
    font_form = SettingFontForm(request.POST or None)

    if request.method == 'POST':
        if 'color_submit' in request.POST:
            color_form = SettingColorForm(request.POST)
            if color_form.is_valid():
                # Deactivate all current colors
                SettingColorTable.objects.all().update(active=0)
                # Get the selected color ID from the form
                selected_color =color_form.cleaned_data['color']
        
                # Retrieve the selected color object
                # Set the selected color as active and save it
                selected_color.active = 1
                selected_color.save()
                # Render the template with the updated color
            return redirect('background_color_form_views')
        elif 'font_submit' in request.POST:
            font_form = SettingFontForm(request.POST)
            if font_form.is_valid():
                SettingFontTable.objects.all().update(active=0)
                selected_font = font_form.cleaned_data['font']
                font_form = selected_font
                selected_font.active = 1
                selected_font.save()
            return redirect('background_color_form_views')

    return render(request, 'color_background.html', {
        'color_form': color_form,
        'font_form': font_form,
        'selected_color': selected_color,
        'selected_font': selected_font
    })