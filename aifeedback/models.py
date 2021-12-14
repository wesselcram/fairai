from django.db import models

# Create your models here.
class Instances2(models.Model):
	instanceid			= models.AutoField(primary_key=True)
	c_charge_degree		= models.CharField(max_length=20)
	race				= models.CharField(max_length=20)
	sex					= models.CharField(max_length=20)
	age					= models.IntegerField()
	priors_count		= models.IntegerField()
	recidivism			= models.BooleanField()

class Counterfactuals2(models.Model):
	instanceid			= models.ForeignKey(Instances2, on_delete=models.CASCADE)
	Counterfactualid	= models.AutoField(primary_key=True)
	c_charge_degree		= models.CharField(max_length=20)
	race				= models.CharField(max_length=20)
	sex					= models.CharField(max_length=20)
	age					= models.IntegerField()
	priors_count		= models.IntegerField()
	recidivism			= models.BooleanField()
	BOOL_CHOICES = [ 
		(0, 'false'), 
		(1, 'true')]
	fair				= models.BooleanField(choices=BOOL_CHOICES, null=True, default=None)
