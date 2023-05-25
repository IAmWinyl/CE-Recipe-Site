from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Remove this
        print(username, password)

        # Remove this
        user = authenticate(request,username=username,password=password)

        if user is None:
            context['error'] = "Incorrect username and/or password."
        else:
            login(request, user)
            return redirect("/")
        
    return render(request,"accounts/login.html",context=context)

def logout_view(request):
    context = {}
    if request.method == "POST" and request.user.is_authenticated:
        logout(request)
        return redirect("/")
    return render(request,"accounts/logout.html",context)


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save()
        return redirect("/login")
    context = {
        "form" : form
    }
    return render(request,"accounts/register.html",context)