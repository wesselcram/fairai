from django.forms import ModelForm
from django import forms
from aifeedback.models import *

class CounterfactualsForm(ModelForm):
	class Meta:
		model 	= Counterfactuals2
		fields 	= ['instanceid', 'Counterfactualid', 'c_charge_degree', 'race','sex', 'age', 'priors_count', 'recidivism', 'fair']
		widgets = {'fair'				: forms.RadioSelect(attrs={ 'required': 'true' }),
					'c_charge_degree'	: forms.TextInput(attrs={ 'readonly': 'readonly' }),
					'race'				: forms.TextInput(attrs={ 'readonly': 'readonly' }),
					'sex'				: forms.TextInput(attrs={ 'readonly': 'readonly' }),
					'age'				: forms.TextInput(attrs={ 'readonly': 'readonly' }),
					'priors_count'		: forms.TextInput(attrs={ 'readonly': 'readonly' }),
					'recidivism'		: forms.TextInput(attrs={ 'readonly': 'readonly' }),
					'instanceid'		: forms.HiddenInput(),
					}
		
class InstanceForm(ModelForm):
	class Meta:
		model 	= Instances2
		fields 	= ['c_charge_degree', 'race','sex', 'age', 'priors_count', 'recidivism']
		widgets = {'c_charge_degree'	: forms.TextInput(attrs={ 'readonly': 'readonly' }),
					'race'				: forms.TextInput(attrs={ 'readonly': 'readonly' }),
					'sex'				: forms.TextInput(attrs={ 'readonly': 'readonly' }),
					'age'				: forms.TextInput(attrs={ 'readonly': 'readonly' }),
					'priors_count'		: forms.TextInput(attrs={ 'readonly': 'readonly' }),
					'recidivism'		: forms.TextInput(attrs={ 'readonly': 'readonly' }),
					}
