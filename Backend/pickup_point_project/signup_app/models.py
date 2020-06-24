# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from enum import Enum
#
#
#
# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, full_name, phone, password=None):
#         if not email:
#             return ValueError("User must have an email address")
#         if not full_name:
#             return ValueError("User must enter their name")
#         if not phone:
#             return ValueError("User must enter the phone number")
#
#         user = self.model(
#             email=self.normalize_email(email),
#             full_name=full_name,
#             phone=phone
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return
#
#     def create_superuser(self, email, full_name, phone, password=None):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             full_name=full_name,
#             phone=phone,
#             password=password,
#         )
#         user.save(using=self._db)
#         return user
#
#
# class Users(AbstractBaseUser):
#     # id = models.IntegerField(primary_key=True)
#     full_name = models.CharField(max_length=500)
#     email = models.EmailField(max_length=60, unique=True)
#     phone = models.CharField(max_length=16)
#     # hash = models.TextField(max_length=256)
#     # salt = models.TextField(max_length=32)
#     # onboarded_at = models.DateTimeField(auto_now=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELD = ['full_name', 'phone']
#
#     objects = MyAccountManager()
#
#
# # class Locations(models.Model):
# #     id = models.IntegerField(primary_key=True)
# #     longitude = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
# #     latitude = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
