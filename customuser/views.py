from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.views.decorators.http import require_http_methods, require_safe
from django.conf.urls import handler500
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserEditForm, UserProfileForm


# Create your views here.
@require_safe
def home(request):
    try:
        return render(request, 'home.html')
    except Exception:
        return redirect(handler500)

@require_safe
def aboutus(request):
    try:
        return render(request, 'aboutus.html')
    except Exception:
        return redirect(handler500)
    

@require_http_methods(["GET","POST"])
def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


@transaction.atomic
@require_http_methods(["GET","POST"])
def signup(request):
    try:
        if request.method == 'GET':
            user_form = SignUpForm()
            custom_user_form = UserProfileForm()
            return render(request, 'signup.html', {"u_form": user_form, "c_form": custom_user_form})
        if request.method == 'POST':
            user_form = SignUpForm(request.POST)
            custom_user_form = UserProfileForm(request.POST)

            if user_form.is_valid() and custom_user_form.is_valid():
                user = user_form.save()

                custom_user = custom_user_form.save(commit=False)
                custom_user.user = user
                custom_user.save()
                return redirect('login')
            else:
                user_form = SignUpForm(request.POST)
                custom_user_form = UserProfileForm(request.POST)

                for field in user_form.errors:
                    user_form[field].field.widget.attrs['class'] += ' error'
                for field in custom_user_form.errors:
                    custom_user_form[field].field.widget.attrs['class'] += ' error'
                return render(request, 'signup.html', {"u_form": user_form, "c_form": custom_user_form})
    except Exception:
        return redirect(handler500)