from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def connection(request):
    if request.method== 'POST':
        name = request.POST['name']
        password = request.POST['password1']
        #predefine fonction from django using from django.contrib.auth import authenticate
        
        user = authenticate(username=name,password=password)
        if user is not None:
            request.method= 'GET'
            return render(request, 'menu.html')
        else:
            return render(request, 'connection.html')
    else:
        return render(request, 'connection.html')

