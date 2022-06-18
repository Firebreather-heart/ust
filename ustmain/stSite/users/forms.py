from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django import forms 

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username','email','date_of_birth','profile_pic','about')
        widget = {
            'username':forms.TextInput(
                attrs={
                    'placeholder':'Username','class':'w3-input w3-border w3-round','type':'text','name':'username',
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'placeholder':'E-mail','class':'w3-input w3-border w3-round','type':'email','name':'email',
                }
            ),
            'date_of_birth' : forms.DateInput(attrs={
            'placeholder':'Date of Birth','class':'w3-input','type':'date','name':'dob'
        }),
            'about':forms.Textarea(
                attrs={
                    'placeholder':'About','class':'w3-input w3-border w3-round','type':'text','name':'about',
                }
            )
            
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username','email','date_of_birth','profile_pic','about')
        widget = {
            'username':forms.TextInput(
                attrs={
                    'placeholder':'Username','class':'w3-input w3-border w3-round','type':'text','name':'username',
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'placeholder':'E-mail','class':'w3-input w3-border w3-round','type':'email','name':'email',
                }
            ),
            'date_of_birth' : forms.DateInput(attrs={
            'placeholder':'Date of Birth','class':'w3-input','type':'date','name':'dob'
        }),
            'about':forms.Textarea(
                attrs={
                    'placeholder':'About','class':'w3-input w3-border w3-round','type':'text','name':'about',
                }
            )
            
        }