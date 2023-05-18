from django.shortcuts import render,redirect

from .forms import *

from .models import *

from django.contrib import messages

from django.contrib.auth import authenticate, login

 

 

from django.conf import settings

from django.core.mail import send_mail

# Create your views here.

def index(request):

    return render(request,'index.html')

 

 

def dashboard(request):

    return render(request,'dashboard.html')

def addpost(request):

        if request.method == 'POST':

                post=posts()

                post.title= request.POST['title']

                post.content= request.POST['content']

                post.save()

                

                return render(request, 'addpost.html')  

 

        else:

                return render(request,'addpost.html')

       

def viewall(request):

    cr=posts.objects.all().order_by('-title')

    #select * from posts order by title

    return render(request,'listall.html',{'cr':cr})

 

def viewone(request):

    if request.method=='POST':

        t=request.POST['title']

        cr=posts.objects.filter(title=t)

        return render(request,'listall.html',{'cr':cr})

    else:

        return render(request,'viewone.html')

 

def deleteone(request):

    if request.method=='POST':

        t=request.POST['title']

        cr=posts.objects.filter(title=t)

        cr.delete()

        #return render(request,'listall.html')

        return render(request,'deleteone.html')

    else:

        

        return render(request,'deleteone.html')

 

 

def register(request):

    form=RegisterForm()

    dict={'form':form}

    if request.method=="POST":

        form=RegisterForm(request.POST)

        if form.is_valid():

            user=form.save()

            user.set_password(user.password)

            subject = 'welcome to FDP'

            message = 'Hi , thank you for registering in FDP.'

            email_from = 'nefsal003@gmail.com'

            recipient_list = [user.email, ]

            send_mail( subject, message, email_from, recipient_list )

            user.save()

            messages.success(request,"succeessfull")

            #return redirect('login')

        

    return render(request,'register.html',dict)

 

def log(request):

    if request.method == 'POST':

        # Process the request if posted data are available

        username = request.POST['username']

        password = request.POST['password']

        # Check username and password combination if correct

        user = authenticate(username=username, password=password)

        if user is not None:

            # Save session as cookie to login the user

            login(request, user)

            # Success, now let's login the user.

            return render(request, 'dashboard.html')

        else:

            # Incorrect credentials, let's throw an error to the screen.

            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})

    else:

        # No post data availabe, let's just show the page to the user.

        return render(request, 'login.html')


def about(request):
     return render(request, 'about.html')

def buy(request):
     return render(request, 'buy.html')

def contact(request):
     return render(request, 'contact.html')

def index(request):
     return render(request, 'index.html')

def medicine(request):
     return render(request, 'medicine.html')

