from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import PassportForm
from django.contrib import messages
from django.views.generic import ListView
from .models import PassportInfo

def passport_new(request):
    if request.method == 'POST':
        form = PassportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'One Information Successfully Added')
<<<<<<< HEAD
            return redirect('/dashboard')
=======
            return redirect('dashboard')
        else:
            print("error", form.errors)
            messages.error(request, 'One Information Add Failed')

>>>>>>> b3900a903d2aea10d825fa0cd6d19d2b49b12cdb
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
                return render(request, 'dashboard.html', {'messages':messages})
            else:
                return render(request, 'login.html', {'error_message':'You account is not active'})

        else:
            return render(request, 'login.html', {'error_message':'Invalid Login'})

    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')


class InfoListView(ListView):
    model = PassportInfo
    template_name = 'info.html'
    context_object_name = 'passportinfos'
