from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	#this is the url to which the confirmation msg goes to
	path('test/', views.test, name="test"),
	path('newsD/<int:news_id>/', views.newsD, name="newsD"),
	#this is the test url
	path('test2/', views.test2, name="test2"),
	path('login/', views.login, name="login"),
	path('authentication/', views.authentication, name="authentication")

]

