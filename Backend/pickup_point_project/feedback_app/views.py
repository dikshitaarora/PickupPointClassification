from django.shortcuts import render
from .apps import FeedbackAppConfig
from django.conf import settings
import pandas as pd
import os
# Create your views here.

def call_model(request):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	path = os.path.join(BASE_DIR, 'acmss.csv')
	f1 = open(path, "r")
	last_line = f1.readlines()[-1]
	last_line=last_line.rstrip("\n")
	w=last_line.split(',')
	l1=w[0:4]
	list1 = [float(x) for x in l1]
	f1.close()

	data = {'a': [list1[0]], 'b': [list1[1]], 'c': [list1[2]], 'd': [list1[3]]}
	df = pd.DataFrame(data)
	predictions = FeedbackAppConfig.Pickle_Model.predict_classes(df)
	if(predictions[0][0]==1):
		str="Not feasible"
		val=False
	elif(predictions[0][0]==0):
		str="feasible"
		val=True
	print(str)
	context={
		"feedback": str,
		"value": val,
    }
	return render(request,'./sugg.html', context)
