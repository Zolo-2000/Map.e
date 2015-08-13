from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from .models import Profile

# Create your views here.

def login(request):
	template = "login.html"	
	return render_to_response(template, {})

# Create your views here.
