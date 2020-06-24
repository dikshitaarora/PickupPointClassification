import os
import urllib.parse as up
import psycopg2

import csv

def csvv():
  con = psycopg2.connect(database="yufgjsqs", user="yufgjsqs", password="C2m8NhHNWMY0q8jCCanfVbFDlNvqq9Wy", host="ruby.db.elephantsql.com", port="5432")
  print("Database opened successfully")

  cur = con.cursor()
  cur.execute("SELECT google_rating, no_of_lockers, no_of_working_hours, no_of_working_days FROM public.registration_app_store ")
  rows = cur.fetchall()

  with open('acmss.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)


  print("Operation done successfully")
  con.close()
