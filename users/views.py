from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth import authenticate, login as auth_login
from .models import Profile
# Create your views here.

def mainLogin(request):
    return render(request, 'main/mainLogin.html')



def approveAccount(request):
    seniors = User.objects.all().order_by('-id')
    
    context = {
        'seniors': seniors
    }
    
    return render(request, 'main/approve.html', context)


def inputData(request):
    
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic') 
        fullname = request.POST['fullname']
        phone_num = request.POST['phone_num']
        dob = request.POST['dob']
        purok = request.POST['purok']
        address = request.POST['address']
        barangay = request.POST['barangay']
        postal_code = request.POST['postal_code']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=phone_num).exists():
                messages.error(request, 'Phone number already taken.')
                return redirect(request.META.get('HTTP_REFERER'))

            else:
                seniors = User.objects.create_user(
                    first_name=fullname, username=phone_num, password=password1, is_staff=False, is_superuser=False )
                seniors.save()
                
                new_profile = Profile.objects.create(
                    name=seniors, profile_pic=profile_pic,address=address, dob=dob, purok=purok, barangay=barangay, postal_code=postal_code)
                new_profile.save()
                messages.success(request, 'Account created')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Password does not match.')
            return redirect(request.META.get('HTTP_REFERER'))

    
    return render(request, 'main/inputData.html')


def mainDashboard(request):
    users = User.objects.all().order_by('-id')
    
    context = {
        'users': users
    }
    
    return render(request, 'main/index.html', context)

def login(request):
    if request.method == 'POST':
        phone_num = request.POST.get('phone_num')
        password = request.POST.get('password')

        info = authenticate(username=phone_num, password=password)
        if info is not None:
            auth_login(request, info)
            if info.is_staff:
                return redirect('seniorDashboard')
            else:
                messages.error(request, "You are not approve to the admin. Please wait")
                return redirect('login')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('login')
    return render(request, 'login.html')
    
def homepage(request):
    
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic') 
        fullname = request.POST['fullname']
        phone_num = request.POST['phone_num']
        dob = request.POST['dob']
        purok = request.POST['purok']
        address = request.POST['address']
        barangay = request.POST['barangay']
        postal_code = request.POST['postal_code']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=phone_num).exists():
                messages.error(request, 'Phone number already taken.')
                return redirect('register')

            else:
                seniors = User.objects.create_user(
                    first_name=fullname, username=phone_num, password=password1, is_staff=False, is_superuser=False )
                seniors.save()
                
                new_profile = Profile.objects.create(
                    name=seniors, profile_pic=profile_pic,address=address, dob=dob, purok=purok, barangay=barangay, postal_code=postal_code)
                new_profile.save()
                messages.success(request, 'Account created')
                return redirect('login')
        else:
            messages.error(request, 'Password does not match.')
            return redirect('register')
    return render(request, 'register.html')


def seniorDashboard(request):
    return render(request, 'seniors/index.html')



def removeUser(request, user_id):
    User.objects.filter(id=user_id).delete()
    messages.success(request, 'User Removed')
    return redirect(request.META.get('HTTP_REFERER'))


def acceptUser(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_staff = True
    user.save()
    # You can redirect to a success page or to the same page
    messages.success(request, 'Senior Citizen Approved')
    return redirect(request.META.get('HTTP_REFERER'))

def declineUser(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_staff = False
    user.save()
    # You can redirect to a success page or to the same page
    messages.error(request, 'Senior Citizen Rejected')
    return redirect(request.META.get('HTTP_REFERER'))

def logoutUser(request):
    auth.logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('homepage')