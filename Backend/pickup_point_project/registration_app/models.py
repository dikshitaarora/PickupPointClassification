from django.db import models

# Create your models here.
state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))


class Address(models.Model):
	id = models.AutoField(primary_key=True)
	first_line = models.CharField(max_length=500)
	city = models.CharField(max_length=500)
	state = models.CharField(choices=state_choices, max_length=255, null=True, blank=True)
	pin_code = models.CharField(max_length=10)
	country_code = models.CharField(max_length=3)


class Partner(models.Model):
	id = models.AutoField(primary_key=True)
	phone = models.CharField(max_length=12)
	email = models.EmailField(max_length=60, unique=True)






class Store(models.Model):
	id = models.AutoField(primary_key=True)
	partner_id = models.ForeignKey(Partner, on_delete=models.CASCADE)
	store_name = models.CharField(max_length=256)
	address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
	store_type = models.CharField(max_length=500)
	open_time = models.TimeField(null=True, blank=True)
	close_time = models.TimeField(null=True, blank=True)
	no_of_lockers = models.IntegerField()
	time_zone = models.CharField(max_length=500)
	dimension= models.CharField(max_length=50)
	no_of_working_days=models.IntegerField()
	no_of_working_hours=models.IntegerField()
	google_rating = models.IntegerField()
	exist= models.CharField(max_length=4)
