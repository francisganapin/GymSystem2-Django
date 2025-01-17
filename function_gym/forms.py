from django import forms
from .models import GymMember

class MemberLoginForm(forms.Form):
   id_card = forms.CharField(label="ID Card", max_length=50, required=True)

   class Meta:
      model = GymMember

class MemberRegisterForm(forms.ModelForm):
   
    class Meta:
            model = GymMember
            fields = '__all__'
            widgets = {
                'expiry':forms.DateInput(attrs={'type':'date'}),
            }

    def clean_expiry(self):
        expiry = self.cleaned_data.get('expiry')
        if not expiry:
                raise forms.ValidationError('expiration date is required boss')
        return expiry