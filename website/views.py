from django.shortcuts import render
from django.core.mail import send_mail
from .models import Form

def index(request):
	return render(request, 'website/index.html')	

def test(request):
	if request.method == "POST":
		name=request.POST['name']
		email=request.POST['email']
		date=request.POST['date']
		drop=request.POST.get('drop', False)
		phone=request.POST['phone']
		message1=request.POST['message']
		
		message = "Name: "+ name + "\n" + "email: "+ email + "\n" + "Date of appointment: " + date + "\n" + "Service: " + drop + "\n" + "Number: " + phone + "\n" + "Special Message: "+ message1

		#send an email
		send_mail(
			'Make appointment for ' + name, #subject
			message, #the msg
			email, #from email
			['madhavm2002@gmail.com'] #to email
			)
		form=Form(name = name, email = email, date = date, drop = drop, phone = phone, msg1= message1)
		form.save()
		return render(request, 'website/test.html', {'name':name})
	else:
		return render(request, 'website/index.html')

def newsD(request):
	return render(request, 'website/newsD.html', {})