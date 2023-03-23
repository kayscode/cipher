from django.shortcuts import render, redirect

# models
from .models import User

# import form
from chat.forms import UserForm

# utils
from cracker.app.security import SecurityPolice
from cracker.app.Timer import Timer
from cracker.app.generator import generate_password


# Create your views here.
def index(request):
    return render(request, "chat/index.html")


def login(request):
    pass


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
                # test if the password provided is strong
                timer = Timer(30)
                result = timer.start_timer(user_form.cleaned_data["password"], generate_password)
                if not result["is_password_strong"]:
                    user = User.objects.get(user_form.cleaned_data["email"])
                    user.delete()
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
