from django.shortcuts import render,redirect
from django.contrib.auth.models import User


#focnction which create a user 
def register(request):
    if request.method=='POST':#verify if the method is post
        #affecting the values enter by the user to be save in the BD
        name = request.POST['username']
        password_1= request.POST['password_1']
        password_2= request.POST['password_2']
        email=request.POST['email']

        if password_1==password_2:
            if User.objects.filter(username = name):
                print('user name already exist ')
            else: 
                user = User.objects.create_user(username=name, password=password_1, email=email)
                user.save()
                print('user created')
                request.method='GET'
                return render(request,"menu.html")
        else:
            print('password not matching...')
        return render(request, 'connect/register.html')
    
    else:
        return render(request,"connect/register.html")
    

# Create your views here.