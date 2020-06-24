from django.apps import AppConfig
from django.conf import settings
import os
import pickle

class FeedbackAppConfig(AppConfig):
	name = 'feedback_app'
	path = os.path.join(settings.MODELS,'Pickle_Model.pkl')
	# load models into separate variables
	# these will be accessible via this class
	with open(path,'rb') as pickled:
		Pickle_Model = pickle.load(pickled)
