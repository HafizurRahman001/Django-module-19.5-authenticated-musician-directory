from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,update_session_auth_hash,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from authentication.forms import SignUpForm

# Create your views here.

def user_signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request,"Account Created Successfully")
            return redirect('login')
    else:
        signup_form = SignUpForm()
    return render(request,'login_signup_form.html', {'form':signup_form, 'type':'Signup'})



def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data = request.POST)
        if login_form.is_valid():
            userName = login_form.cleaned_data['username']
            userPass = login_form.cleaned_data['password']
            user = authenticate(username = userName, password = userPass)
            if user is not None:
                messages.success(request, "You loged in successfully")
                login(request,user)
                return redirect('profile')
    else:
        login_form = AuthenticationForm()
    return render(request,'login_signup_form.html',{'form':login_form, 'type':'Login'})



def user_logout(request):
    logout(request)
    messages.success(request,"You loged out successfully")
    return redirect('login')


def profile(request):
    return render(request,'profile.html')
