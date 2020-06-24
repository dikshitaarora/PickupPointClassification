from django.shortcuts import render,redirect
from .models import Address
from .models import Partner
from .models import Store
from .ccsv import csvv


# Create your views here.

def register(request):
    return render(request, './shopdetails.html')


def frame(request):
    return render(request, './registrationframe.html')

def sugg(request):
	return render(request,'./sugg.html')

def registered(request):
	if request.method == 'POST':

		first_line = request.POST["locality"]
		city = request.POST["city"]
		state = request.POST["state"]
		pin_code = request.POST["pin_code"]
		country_code = request.POST["countryCode"]
		address = Address(first_line=first_line, city=city, state=state, pin_code=pin_code, country_code=country_code)
		address.save()

		email = request.POST["email"]
		phone = request.POST["phone"]
		partner = Partner(email=email, phone=phone)
		partner.save()


		address_id_id= address.id
		partner_id_id= partner.id
		store_name = request.POST["company"]
		time_zone = request.POST["time_zone"]
		store_type = request.POST["store_type"]
		no_of_lockers = request.POST["locker"]
		dimension=request.POST["dimension"]
		google_rating = request.POST["googleRating"]
		no_of_working_days=request.POST["working_days"]
		no_of_working_hours=request.POST["working_hours"]
		open_time=request.POST["open_time"]
		close_time=request.POST["close_time"]
		exist=request.POST["exist"]

		store = Store(store_name=store_name,partner_id_id=partner_id_id, address_id_id=address_id_id,store_type =store_type, dimension=dimension,google_rating=google_rating,no_of_working_days=no_of_working_days,no_of_working_hours=no_of_working_hours,time_zone=time_zone, no_of_lockers=no_of_lockers,open_time=open_time,close_time=close_time,exist=exist)
		store.save()
		csvv()
	response = redirect('/feedback/classify/')
	return response
