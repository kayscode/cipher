from django.shortcuts import render, redirect

# models
from .models import User
from django.db import models
# import form
from chat.forms import UserForm, UserLoginForm

# utils
from cracker.app.security import SecurityPolice
from cracker.app.Timer import Timer
from cracker.app.generator import generate_password

# Create your views here.
def index(request):
    return render(request, "chat/index.html")


def login(request):
    user_login_form = UserLoginForm()
    more_errors = list();
    if request.method == "POST":
        user_login_form = UserLoginForm(request.POST, request.FILES)
        
        if user_login_form.is_valid():
            # user = User.objects.filter(email = user_login_form.cleaned_data.get("email")).get()

            try:
                user = User.objects.filter(email = user_login_form.cleaned_data.get("email")).get()
            except User.DoesNotExist:
                user = None
            # print(user.password, user.email)

            if user and user.password == user_login_form.cleaned_data.get("password"):
                return redirect("discussions_index")
            
            if not user:
                more_errors.append("user doesn't exist")
            
            if user and user.password != user_login_form.cleaned_data.get("password"):
                more_errors.append("password doesn't match")

    context = {"form":user_login_form, "more_errors":more_errors}
    return render(request,'chat/auth/login.html',context)


def signup(request):
    user_form = UserForm()
    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES)
        if user_form.is_valid():
            # check if user data respect the policy

            user_data = user_form.cleaned_data
            policy_tester = SecurityPolice(
                first_name=user_data.get("first_name"),
                last_name=user_data.get("last_name"),
                password=user_data.get("password")
            )
            if policy_tester.is_password_respect_policy():
                user_form.save()
                # test if the password provided is strong and return an dict with key is_password_strong
                timer = Timer(5)
                result = timer.start_timer(user_form.cleaned_data["password"], generate_password)
                if not result["is_password_strong"]:
                    user = User.objects.get(user_form.cleaned_data["email"])
                    user.delete()
                    redirect("password_failed_message")
                print(result)

            else:
                print(policy_tester.get_errors())
                # user_form.more_errors = policy_tester.get_errors()
                return render(request, "chat/auth/signup.html",
                              {"more_errors": policy_tester.get_errors(), "user_form": user_form})

            # dictionary
            # bruteforce attac
            # print(user_form.cleaned_data)
            return redirect("chat_index")

    context = {'user_form': user_form}
    return render(request, "chat/auth/signup.html", context)


def logout(request):
    pass


def discussions_index(request):
    """
        this views is in charge of rendering the index page of discussions with
        the list of all the users
    """
    users = User.objects.all()

    context = {"users" : users}
    return render(request, "chat/discussions/index.html",context)