from django.db import models

class Form(models.Model):
	msg_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=80)
	email = models.CharField(max_length=80)
	date = models.CharField(max_length=80)
	drop = models.CharField(max_length=80)
	phone = models.CharField(max_length=80)
	msg1 =  models.CharField(max_length=500)
