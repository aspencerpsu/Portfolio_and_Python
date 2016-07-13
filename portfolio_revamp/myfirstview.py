from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader

def sometext(request):
	return render_to_response('samplehtml.html', {'owner': 'John Marcellus', 'books':'The Kiterunner', 'author':'Khaled Hosseini'})


def index(request):
	index = open(r'templates/home.html').read()
	return HttpResponse(index)