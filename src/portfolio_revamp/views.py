import sys
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.template import loader, Context, Engine, TemplateDoesNotExist
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.template import RequestContext
from django.conf.urls import handler404, handler500
from django.views.decorators.clickjacking import xframe_options_exempt

#from blogs.models import Blogs
from tweepy import API
import tweepy

#sys.path.append("C:/Python27/Lib/site-packages/django/bin/")

auth = tweepy.OAuthHandler("pX0OETs87mPD0CROfEl5xNSKL", "wOokX8k54HrrWEXGORnarOYzZFiISSVxT90xOJgvX3FcMUX0QB")

auth.set_access_token("457888099-zEIwcezHpVbznLivoMfZ0dzXUgZdN8w3DfcFP1Kl", "cfsPMsazvavdOMQnZUoRUSVzoZHnmuyOv0Kw0UDP1kBSg")

api = tweepy.API(auth)

def main(request):
	last_5 = api.user_timeline(457888099, None, None, 6, None)
	second_tweet = last_5[1]
	
	context = {
			"last_5": last_5,
			"second_tweet": second_tweet,
			"title": "Spencer Tech Consulting Homepage",
		}

	return render(request, "main.html", context)

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
	return render(request, 'list.html')


@xframe_options_exempt
def about(request):
	"""The following will have some testimonials of what I've done
	   and also showcase current projects I'm working on"""
	
	context = {"title": "What SpencerTech Does"}

	return render(request, 'about.html', context)

def contacts(request):
	""" Just some information
	    about myself, including my gmail account and phonenumber"""
	context = {"title": "How To Reach Me"}
	return render(request, 'contact.html', context)

def page_cannot_load(request):

	message = u"a bad search by you, the user"

	context = {'request_path': request.path,
				'exception': message}

	try:
		template  = loader.get_template("404.html")
		body = template.render(context, request)
		content_type = "text/html"

	except TemplateDoesNotExist:
		template = Engine().from_string(
			'<h1>Not Found</h1>'
			'<p>The requested URL {{request_path}} was not found on this server.</p>')
		body = template.render(Context(context))
		content_type = 'text/html'
	return HttpResponse(body, content_type=content_type, status=404)



