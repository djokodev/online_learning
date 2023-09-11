from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from . models import CustomUser
#from django_countries.widgets import CountrySelectWidget



class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username", "first_name", "last_name", "email", "country_residence", "profile_picture", "status"]
        
        
        


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, label="Nom d’utilisateur")
    password = forms.CharField(max_length=60, widget=forms.PasswordInput, label="Mot de passe")
    """le parametre widget = forms.PasswordInput cache automatiquement la saisie.
        LoginForm represente notre formulaire de connexion.
    """