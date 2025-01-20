from django import forms
from .models import GymMember

class MemberLoginForm(forms.ModelForm):
    id_card = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter ID Card'}),
        label="ID Card"
    )

    class Meta:
        model = GymMember
        fields = ['id_card']

    def clean_id_card(self):
        id_card = self.cleaned_data.get('id_card', '').strip()
        return id_card

        

class MemberRegisterForm(forms.ModelForm):
   
    class Meta:
            model = GymMember
            fields = ['id_card','expiry','first_name','last_name','gender','phone_number','address','profile_image']
            widgets = {
                'expiry':forms.DateInput(attrs={'type':'date'}),
            }

    def clean_expiry(self):
        expiry = self.cleaned_data.get('expiry')
        if not expiry:
                raise forms.ValidationError('expiration date is required boss')
        return expiry
    