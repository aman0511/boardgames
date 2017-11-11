from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	print("helo")
	return render(request, "main/home.html", {'message': 'hi, there'})

def login(request):
	print('hii')
	return  render(request, "main/login.html")

