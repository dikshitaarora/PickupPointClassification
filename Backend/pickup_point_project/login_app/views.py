from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def login(request):
	val = True
	context={
		"value":val,
	}
	return render(request,'./login.html',context)

def homepage(request):
	return render(request,'./homepage.html')

def checkUser(request):
	if request.method == 'POST':
		login_username = request.POST['username']
		login_password = request.POST['signinPassword']
		user = authenticate(username=login_username, password=login_password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				# print(user.first_name)
				context={
			        "name": user.first_name,
					"username": user.username,
					"email": user.email,
					"date_join": user.date_joined,
			    }
				return render(request,'./homepage.html',context)

			else:
				print("Inactive") # Return a 'disabled account' error message
		else:
			val = False
			context={
				"value":val,
			}
			return render(request,'./login.html',context)
