from django.shortcuts import render
# from .models import Users
from django.contrib.auth.models import User
# Create your views here.
def log(request):
    return render(request,'./signup.html')

def registered(request):
	if request.method == 'POST':
		first_name = request.POST["Name"]
		email = request.POST["signinEmail"]
		username = request.POST["username"]
		password = request.POST["signinPassword"]
		# users = User(first_name=first_name,username=username, email=email, password=password)
		users = User.objects.create_user(first_name=first_name,username=username,email=email,password=password)
		users.save()
		# print(users)
	return render(request,'./registered.html')
