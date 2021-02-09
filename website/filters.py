import django_filters
from .models import *

class timeslotfilter(django_filters.FilterSet):
	class Meta:
		model = timeslot
		fields = '__all__'