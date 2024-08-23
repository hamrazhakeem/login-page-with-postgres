from django.shortcuts import redirect, render
from .forms import Signinform,Signupform
from django.contrib import messages,auth
from .models import User
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def signin(request):
    if 'username' in request.session:
        return redirect('home')
    if 'uname' in request.session:
        return redirect('customadmin:adminhome')
    if request.method == 'POST':
        form = Signinform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user_exists = User.objects.filter(username=username, password=password).exists()
            
            if user_exists:
                user = User.objects.get(username=username)
                request.session['uid'] = user.id
                request.session['firstname'] = user.firstname
                request.session['lastname'] = user.lastname
                request.session['username'] = user.username
                request.session['email'] = user.email
                return redirect('home')
                
            else:
                messages.error(request,'Invalid username or password.')
        
    else:
        form = Signinform()

    return render(request, 'authentication/signin.html', {'form':form})

@never_cache
def signup(request):
    if 'username' in request.session:
        return redirect('home')
    else:
        if request.method == "POST":
            form = Signupform(request.POST)
            if form.is_valid():
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']

                if confirm_password!=password:
                    messages.success(request, "Password's doesn't match")
                    return redirect('signup')
                else:
                    form.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('signin')
        else:
            form = Signupform()

    return render(request,'authentication/signup.html',{'form': form})

@never_cache
def home(request):
    if 'uid' in request.session: 
        firstname = request.session.get("firstname")
        return render(request, 'authentication/home.html', {'firstname': firstname})
    else:
        return redirect('signin')

def signout(request):
    if 'uid' in request.session:
        request.session.flush()
    messages.success(request,'You have logged out successfully')
    return redirect('signin')

@never_cache
def profile(request):
    if 'uid' not in request.session:
        return redirect('signin')
    user_id = request.session.get("uid")
    try:
        user = User.objects.get(id = user_id)
    except:
        return redirect('signin')
    
    
    return render(request, 'authentication/profile.html', {'user':user})