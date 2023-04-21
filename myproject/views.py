from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User, Login, ButtonClick

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_console')
            else:
                return redirect('user_landing')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

@login_required
def admin_console(request):
    users = User.objects.all()
    logins = Login.objects.all()
    button_clicks = ButtonClick.objects.all()
    return render(request, 'admin_console.html', {'users': users, 'logins': logins, 'button_clicks': button_clicks})

@login_required
def user_landing(request):
    return render(request, 'user_landing.html')

@login_required
def button_click(request, button_id):
    button_click = ButtonClick(user=request.user, button_id=button_id)
    button_click.save()
    return redirect('user_landing')

def logout_view(request):
    logout(request)
    return redirect('index')
