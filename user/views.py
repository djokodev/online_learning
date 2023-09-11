from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.conf import settings


# fontion de deconnexion d'un utilisateur et de redirection vers la l'acceuil
def logout_user(request):
    logout(request)
    return redirect('login')



def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    return render(request, "user/signup.html", {"form":form})



def login_page(request):
    form = forms.LoginForm() # ici je recupere mon formulaire de connexion
    message = ""
    
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate( #Si les identifiants sont corrects, elle retourne l’utilisateur correspondant aux identifiants. Sinon, elle retourne None.
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                message = 'Identifiants invalides.'
                
    return render(request, 'user/login.html', {"form":form, "message":message})
