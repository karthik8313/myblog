from django.shortcuts import render,redirect
from .models import blogpost
from django.http import HttpResponse

def index(request):
	post = blogpost.objects.all()
	return render(request,"index.html",{'post':post})
def detail(request):
	return render(request,"detail.html")
def home(request):
	return redirect(index)