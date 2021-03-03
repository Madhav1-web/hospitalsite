from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Form, categories, Doctors, News, timeajax, dateajax
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
import json as simplejson
from django.http import HttpResponse
from django.core import serializers

def index(request):
	det= dateajax.objects.all()
	newss= News.objects.all()
	doctor = Doctors.objects.all()
	doctor_count=Doctors.objects.count
	item  = categories.objects.all() # use filter() when you have sth to filter ;)
	if request.method == 'POST':
		selected_item = get_object_or_404(Item, pk=request.POST.get('item_id'))
		selected_item3 = get_object_or_404(det, pk=request.POST.get('det_id'))
		# get the user you want (connect for example) in the var "user"
		dateajax.item=selected_item3
		dateajax.save()
		categories.item = selected_item
		categories.save()

		# Then, do a redirect for example

	return render(request, 'website/index.html', {'items':item, 'doctor':doctor, 'doctor_count':doctor_count, 'newss':newss, 'det':det })	

def test(request):
	dt_for_upd=request.POST.get('drop1', False)
	time_for_upd = request.POST.get('drop2', False)
	
	selected_date = dateajax.objects.get(dateaj = dt_for_upd)
	status_upd = timeajax.objects.filter(dateajax=selected_date, timeaj=time_for_upd).update(status=1)
	

	if request.method == "POST":
		name=request.POST['name']
		email=request.POST['email']
		drop=request.POST.get('drop', False)
		date=request.POST.get('drop1', False)
		time=request.POST.get('drop2', False)
		phone=request.POST['phone']
		message1=request.POST['message']
		
		message = "Name: "+ name + "\n" + "email: "+ email + "\n" + "Date of appointment: " + date + "\n" + "Time: " + time + "\n" "Service: " + drop + "\n" + "Number: " + phone + "\n" + "Special Message: "+ message1

		#send an email
		send_mail(
			'Make appointment for ' + name, #subject
			message, #the msg
			email, #from email
			['madhavm2002@gmail.com'] #to email
			)
		#this is used to get the class from the models and then uses the variables assigned here to give value to the variables in models
		form=Form(name = name, email = email, date = date, time= time, drop = drop, phone = phone, msg1= message1)
		#this used the save method to save the object into the database
		form.save()
		#this is for changing status but it is creating new objects so im commenting it out
		'''
		selected_date = dateajax.objects.get(dateaj = date)
		status_upd= timeajax(dateajax= selected_date, timeaj=time)
		status_upd.status=1
		status_upd.save()	
		'''
		
		return render(request, 'website/test.html', {'name':name})
	else:
		return render(request, 'website/index.html')
	
	print("hello")	

def newsD(request, news_id):
	newss=get_object_or_404(News, pk=news_id)
	return render(request, 'website/newsD.html', {'newss':newss})

def test2(request):
	det= dateajax.objects.all()
	newss= News.objects.all()
	doctor = Doctors.objects.all()
	doctor_count=Doctors.objects.count
	item  = categories.objects.all() # use filter() when you have sth to filter ;)
	if request.method == 'POST':
		selected_item = get_object_or_404(Item, pk=request.POST.get('item_id'))
		selected_item3 = get_object_or_404(det, pk=request.POST.get('det_id'))
		# get the user you want (connect for example) in the var "user"
		dateajax.item=selected_item3
		dateajax.save()
		categories.item = selected_item
		categories.save()
		# Then, do a redirect for example

	return render(request, 'website/test2.html', {'items':item, 'doctor':doctor, 'doctor_count':doctor_count, 'newss':newss, 'myfilter':myfilter, 'det':det })

def login(request):
	return render(request, 'website/login.html', {'form':UserCreationForm()})

def authentication(request):
	disp = Form.objects.all()
	if 	request.method == "POST":
		username1 = request.POST['name']
		user = authenticate(request, username=request.POST['name'], password=request.POST['pwd'])
		if user is None:
			return render(request, 'website/login.html', {'form':UserCreationForm(), 'error':"Username and password do not match"})
		else:
			return render(request, 'website/auth.html', {'me': username1, 'disp':disp })	
	else:
		return render(request, 'website/login.html', {})
				
	
def load_time(request):
	sel_day = request.GET.get('tim', None)
	result_set = []
	all_cities = []
	selected_date = dateajax.objects.get(dateaj = sel_day)
	times = timeajax.objects.filter(dateajax=selected_date, status=0).all()
	for time in times:
		result_set.append(time)
	data = serializers.serialize('json', result_set)
	return HttpResponse(data, content_type='application/json')