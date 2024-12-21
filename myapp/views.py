from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def index(request):
    # name = "harini"
    # return render(request,'index.html',{'name':name})

    data = {
        'name':"Harini",
        'age':24,
        'nationality':"indian"
    }
    return render(request,'index.html',data)

def counter(request):
    text =  request.POST['text']
    amount_of_words = len(text.split())
    return render(request,'counter.html',{'amount':amount_of_words})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')  # This checks if the email already exists
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                # Create user without passing password2
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

              

def login(request):

    if request.method == 'POST':
        username = request.POST['username']  # Assuming email is used as username
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)  # Authenticate using username

        if user is not None:  # This is for correct user
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Please sign up')
            return redirect('login')  # This is for users who are not signed up
    else:
        return render(request, 'login.html')





   