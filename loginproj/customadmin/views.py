from django.shortcuts import redirect, render
from authentication.forms import Signinform,Signupform
from customadmin.forms import Usereditform
from django.contrib import messages
from django.views.decorators.cache import never_cache
from authentication.models import User
from django.db.models import Q

@never_cache
def adminsignin(request):
    username = 'hamraz'
    password = '123'

    if 'uname' in request.session and request.session['uname'] == username:
        return redirect('customadmin:adminhome')

    if request.method == 'POST':
        form = Signinform(request.POST)
        if form.is_valid():
            entered_username = form.cleaned_data['username']
            entered_password = form.cleaned_data['password']

            if username == entered_username and password == entered_password:  
                request.session['uname'] = entered_username                  
                return redirect('customadmin:adminhome')
            else:
                messages.error(request, 'Invalid username or password')
    
    form = Signinform()

    return render(request, 'customadmin/adminsignin.html', {'form': form})

@never_cache
def adminhome(request):
    username = 'hamraz'
    if request.session.get('uname') != username:
        return redirect('customadmin:adminsignin')
    return render(request, 'customadmin/adminhome.html')

def adminsignout(request):
    if 'uname' in request.session:
        request.session.flush()
    messages.success(request,'You have logged out successfully')
    return redirect('customadmin:adminsignin')

@never_cache
def manageusers(request):
    if 'uname' not in request.session:
        return redirect('customadmin:adminsignin')

    query = request.GET.get('q')
    users = User.objects.all()

    if query:
        users = users.filter(Q(username__icontains=query))

    context = {'users': users, 'query': query}

    return render(request, 'customadmin/manageusers.html', context)
    
def deleteuser(request,userid):
    user = User.objects.get(id = userid)
    user.delete()
    messages.success(request,'Deleted user Successfully')
    return redirect('customadmin:manageusers')

@never_cache
def edituser(request, userid):
    if 'uname' not in request.session:
        return redirect('customadmin:adminsignin')
    try:
        user_instance = User.objects.get(id=userid)
    except User.DoesNotExist:
        return redirect('customadmin:manageusers')
    if request.method == 'POST':
        form = Usereditform(request.POST, instance=user_instance)
        if form.is_valid():
            form.save()
            messages.success(request,'User details have been updated Successfully')
            return redirect('customadmin:manageusers') 
    else:
        form = Usereditform(instance=user_instance)

    return render(request, 'customadmin/edituser.html', {'form': form})

@never_cache
def createuser(request):
    if 'uname' not in request.session:
        return redirect('customadmin:adminsignin')
    else:
        if request.method == "POST":
            form = Signupform(request.POST)
            if form.is_valid():
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']

                if confirm_password!=password:
                    messages.error(request, "Password's doesn't match")
                    return redirect('customadmin:createuser')
                else:
                    form.save()
                    messages.success(request, 'User created Successfully')
                    return redirect('customadmin:adminhome')
        else:
            form = Signupform()

        return render(request,'customadmin/createuser.html',{'form': form})


          