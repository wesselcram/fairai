from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from django.forms import modelformset_factory

import csv

from .models import *
from .forms import *

def index(request):

	context = {}
	return render(request, 'aifeedback/index.html', context)

def vragenlijst(request):
	
	#formset maken
	counterfactualsFormSet = modelformset_factory(Counterfactuals2, form=CounterfactualsForm, max_num=5)
	
	#we krijgen ingevuld formulier
	if request.POST: 
		formset = counterfactualsFormSet(request.POST) 
		
		#indien geldig, opslaan
		if formset.is_valid():
			formset.save()
		else:
			raise forms.ValidationError("ongeldige data")

	#uitzoeken welke counterfactuals niet zijn ingevuld 
	nietingevuld = Counterfactuals2.objects.filter(fair__isnull=True).values_list('instanceid', flat=True)
	
	#random instance selecteren
	randomInstance = nietingevuld.order_by("?")[0]

	#counterfactualquery maken
	instance = Instances2.objects.get(instanceid=randomInstance)
	counterfactuals = Counterfactuals2.objects.filter(instanceid=instance)
	
	#formset invullen
	formset = counterfactualsFormSet(queryset=counterfactuals)
	
	#instance form maken heel verwarrend omdat instance dit keer twee betekenissen heeft. Deze wordt getoond, maar hoeft niet aangepast te worden
	formIn = InstanceForm(instance=instance)

	#spullen aan context meegeven
	context = {}
	context['formIn'] 		= formIn
	context['formsetCf'] 	= formset

	return render(request, 'aifeedback/vragenlijst.html', context)

def export_csv(request):



	# Create the HttpResponse object with the appropriate CSV header.
	data = download_csv(request)
	#response = HttpResponse(data, content_type='text/csv')
		

	return data
	#return response
  
def download_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="export.csv"'

	queryset = Counterfactuals2.objects.all()
	
	response.write('"instanceid_id","Counterfactualid","c_charge_degree","race","sex","age","priors_count","recidivism","fair"\n')
	
	for row in queryset:
		response.write('"' + '","'.join([
			str(row.instanceid_id), 
			str(row.Counterfactualid),
			str(row.c_charge_degree),
			str(row.race),
			str(row.sex),
			str(row.age),
			str(row.priors_count),
			str(row.recidivism),
			str(row.fair)]) + '"\n')

	return response
 