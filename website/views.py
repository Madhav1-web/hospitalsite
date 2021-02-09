from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Form, categories, Doctors, News, timeslot
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .filters import timeslotfilter

def index(request):
	time = timeslot.objects.all().filter(status=0) #this is for the time objects from database
	newss= News.objects.all()
	doctor = Doctors.objects.all()
	doctor_count=Doctors.objects.count
	item  = categories.objects.all() # use filter() when you have sth to filter ;)
	if request.method == 'POST':
		selected_item2 = get_object_or_404(time, pk=request.POST.get('time_id'))
		selected_item = get_object_or_404(Item, pk=request.POST.get('item_id'))
		# get the user you want (connect for example) in the var "user"
		categories.item = selected_item
		categories.save()
		timeslot.time = selected_item2
		timeslot.save()	

		# Then, do a redirect for example

	return render(request, 'website/index.html', {'items':item, 'doctor':doctor, 'doctor_count':doctor_count, 'newss':newss, 'times':time})	

def test(request):
	if request.method == "POST":
		name=request.POST['name']
		email=request.POST['email']
		date=request.POST['date']
		drop=request.POST.get('drop', False)
		time=request.POST.get('drop1', False)
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
		form.status = 1
		time=timeslot(time = time, date = date, status = 1)
		time.save()
		#this used the save method to save the object into the database
		form.save()
		return render(request, 'website/test.html', {'name':name})
	else:
		return render(request, 'website/index.html')

def newsD(request, news_id):
	newss=get_object_or_404(News, pk=news_id)
	return render(request, 'website/newsD.html', {'newss':newss})

def test2(request):
	time = timeslot.objects.all().filter(status=1) #this is for the time objects from database
	newss= News.objects.all()
	doctor = Doctors.objects.all()
	doctor_count=Doctors.objects.count
	item  = categories.objects.all() # use filter() when you have sth to filter ;)
	myfilter = timeslotfilter()
	if request.method == 'POST':
		selected_item2 = get_object_or_404(time, pk=request.POST.get('time_id'))
		selected_item = get_object_or_404(Item, pk=request.POST.get('item_id'))
		# get the user you want (connect for example) in the var "user"
		categories.item = selected_item
		categories.save()
		timeslot.time = selected_item2
		timeslot.save()	
		# Then, do a redirect for example

	return render(request, 'website/test2.html', {'items':item, 'doctor':doctor, 'doctor_count':doctor_count, 'newss':newss, 'times':time, 'myfilter':myfilter})

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
				