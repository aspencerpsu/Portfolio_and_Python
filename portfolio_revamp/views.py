import sys
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.template import RequestContext
from blogs.models import Blogs

sys.path.append("C:/Python27/Lib/site-packages/django/bin/")

def sometext(request):
	return render_to_response('samplehtml.html', {'owner': 'John Marcellus', 'books':'The Kiterunner', 'author':'Khaled Hosseini'})


def index(request):
	index = open(r'templates/home.html').read()
	paginator = Paginator([Blogs.objects.first()], 1)

	page = paginator.page(1)
	return HttpResponse(index)

def listing(request):
	contact_list = Contacts.objects.all()
	paginator = Paginator(contact_list, 25) #Show 25 contacts per page

	page = request.GET.get('page', 1)
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		#If page is not an integer, deliver first page
		contacts = paginator.page(1)
	except EmptyPage:
		#If page is out of range (e.g. 9999), deliver last page of results
		contacts = paginator.page(paginator.num_pages)
	return render(request, 'list.html', {'contacts': contacts})


