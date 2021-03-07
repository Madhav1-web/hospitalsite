from django.db import models

#the next 2 models are used to test ajax in test2 url
class dateajax(models.Model):
	dateaj = models.CharField(max_length=80)

	def __str__(self):
		return self.dateaj

class timeajax(models.Model):
	dateajax=models.ForeignKey(dateajax, on_delete=models.CASCADE)
	timeaj = models.CharField(max_length=80)
	status = models.IntegerField(default=0)

	def __str__(self):
		return self.timeaj

class Form(models.Model):
	msg_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=80, blank=False)
	email = models.CharField(max_length=80)
	date = models.CharField(max_length=80)
	drop = models.CharField(max_length=80)
	time = models.CharField(max_length=80)
	phone = models.CharField(max_length=80)
	msg1 =  models.CharField(max_length=500)
	status = models.IntegerField(default = 0)
	#these 2 fields are for ajax testing remove after testing
	dateaj = models.ForeignKey(dateajax, on_delete=models.CASCADE, blank=True, null=True)
	timeaj = models.ForeignKey(timeajax, on_delete=models.CASCADE, blank=True, null=True)

class categories(models.Model):
	category = models.CharField(max_length=80)

class Doctors(models.Model):
	doc_id = models.AutoField(primary_key=True)
	dname = models.CharField(max_length=80)
	ddept = models.CharField(max_length=80)
	dphone = models.CharField(max_length=80)
	demail = models.CharField(max_length=80)
	dimage = models.ImageField(upload_to= 'portfolio/images')

class News(models.Model):
	news_id = models.AutoField(primary_key=True)
	ntitle = models.CharField(max_length=80)
	ndesc = models.CharField(max_length=80)
	aname = models.CharField(max_length=80)
	apos = models.CharField(max_length=80)
	aimg = models.ImageField(upload_to= 'portfolio/images')



	
	
