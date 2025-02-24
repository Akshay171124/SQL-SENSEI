from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import Employee
from .models import Users
from .forms import LoginForm
from django.utils.timezone import now

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = Users.objects.get(email=email)
                if check_password(password, user.password):  # Validate hashed password
                    
                    user.last_login_date = now()  # Update last login
                    user.save()
                    login(request, user)
                    request.session['email'] = email
                    request.session.save()

                    return redirect('home')  # Redirect to home page
                else:
                    return render(request, "login.html", {"form": form, "error": "Invalid email or password"})
            except Users.DoesNotExist:
                return render(request, "login.html", {"form": form, "error": "Invalid email or password"})
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    print("User after login:", request.user)
    print("Session ID in home_view:", request.session.session_key)
    print("User is authenticated:", request.user.is_authenticated)
    email = request.session.get('email')
    print("email", email)
    if email:
        try:
            user = Users.objects.get(email=email)  # Get the user based on the email stored in session
            return render(request, "home.html", {"user_name": user.full_name})
        except Users.DoesNotExist:
            return redirect('login')  # If user doesn't exist in the database
    else:
        return redirect('login') 
