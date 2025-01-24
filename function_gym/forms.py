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


    def clean_id_card(self):
        id_card = self.cleaned_data.get('id_card')
        

        if len(id_card) != 10:
            raise forms.ValidationError('The id card must 10 character')
             
        if GymMember.objects.filter(id_card=id_card).exists():
            raise forms.ValidationError('This Card is already Exist')


        return id_card
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        if GymMember.objects.filter(phone_number=phone_number).exists():
             raise forms.ValidationError('this Phone is already Exist')

        return phone_number
    


class GymMembersUpdateForms(forms.ModelForm):
    class Meta:
        model = GymMember
        fields = ['profile_image','expiry']

        widgets ={
            'expiry':forms.DateInput(attrs={'type':'date','class':'form-contro'}),
            'profile_image':forms.FileInput(attrs={'class':'form-control-file'}),
        }