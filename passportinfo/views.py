from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import PassportForm
from django.contrib import messages

@login_required
def passport_new(request):
    if request.method == 'POST':
        form = PassportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'One Information Successfully Added')
            return redirect(' ')
    else:
        form = PassportForm()

    return render(request, 'new_passport.html', {'form':form})


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        u_password = request.POST.get('u_password')
        user = authenticate(username=username, password=u_password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'dashboard.html')
            else:
                return render(request, 'login.html', {'error_message':'You account is not active'})

        else:
            return render(request, 'login.html', {'error_message':'Invalid Login'})

    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
