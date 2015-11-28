from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from .models import Profile

# Create your views here.

def index(request):
	template = "index.html"
	return render_to_response(template, {})

# Create your views here.
