
from django.shortcuts import render, redirect
from .models import AddCamera, ContactUs
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


def add_camera(request):

    rooms = AddCamera.objects.filter()
    # camera_photo = AddCamera.objects.get(id=1)
    return render(request, 'home.html', context={'rooms': rooms})


def Logout(request):
    logout(request)
    x = False
    return redirect('login')


@login_required(login_url='login')
def Main(request):
    x = True
    rooms = AddCamera.objects.filter()
    email = request.user.email
    username = request.user.username
    return render(request, 'main.html', context={'rooms': rooms, 'x': x, 'email': email, 'username': username})


def Login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        x = False
        if user is not None:
            login(request, user)
            return redirect('main')
            # x = True
            # rooms = AddCamera.objects.filter()
            # return render(request, 'main.html', context={'rooms': rooms, 'x': x, 'email': email, 'username': username})
        else:

            return render(request, 'login.html')
    return render(request, 'login.html')


def SignUp(request):
    try:
        if request.method == "POST":
            uname = request.POST.get('username')
            email = request.POST.get('email')
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')
            if pass1 != pass2:
                return render(request, 'signup.html', context={'msg': 'passwords do not match'})
            else:
                my_user = User.objects.create_user(uname, email, pass1)
                my_user.save()

                return redirect('login')
        return render(request, 'signup.html')
    except Exception as msg:
        return render(request, 'signup.html', context={'msg': "Try with different Username"})


@login_required(login_url='login')
def Book(request, email, username):
    subject = "Camera Rental"
    message = f"""Dear {username},
We have received your booking, Kindly wait for Confirmation Mail!"""
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, email_from,
              recipient_list, fail_silently=False)
    return render(request, 'feedback.html', context={'x': True, 'email': email, 'username': username})


@login_required(login_url='login')
def Feedback(request):
    if request.method == "POST":
        fname = request.POST['fname']
        femail = request.POST['femail']
        ffeedback = request.POST['ffeedback']

        f = ContactUs(name=fname, email=femail, feedback=ffeedback)
        f.save()

        subject = "Camera Rental"
        message = f"""Dear {fname},
We have received your feedback, We'll get back to you!!"""
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [femail]

        send_mail(subject, message, email_from,
                  recipient_list, fail_silently=False)
        return render(request, 'feedback.html', context={'x': True})
    return render(request, 'feedback.html', context={'x': True})
