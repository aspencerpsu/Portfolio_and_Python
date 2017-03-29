try:
    from urllib import quote_plus, urlopen #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass

import math
import json
import sys
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
# from comments.models import *

from subscriptions.models import *
from subscriptions.forms import *
from .forms import *
from .models import *
		   
from .utils import *
from django.http import HttpResponse

# Create your views here.
def post_create(request):
	if not request.user.is_staff:
		raise Http404
	
	post_create = request.get_full_path
		
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid() and form.is_bound:
		instance = form.save(commit=False)
		instance.user = request.user
	
		try:
		
			if instance.image.width > 1200 or instance.image.height > 630:
				messages.error(request, "%s  violates image upload constraints"%(instance.image.name))
				return HttpResponseRedirect("/posts/create")
			
			else:
				#change the state of the share grid for post
				# message success
				instance.save()
				messages.success(request, "Successfully Created")
				return HttpResponseRedirect(instance.get_absolute_url())
		except:
			#Perform your logic with the image attribute `blank`
			instance.save()
			messages.success(request, "Successfully Created")
			return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	methods = dir(request)
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
	  ip = x_forwarded_for.split(',')[0]
	else:
	  ip = request.META.get('REMOTE_ADDR')
	subscriptions = Subscription.objects.all().filter(ipadd=ip)
	if len(subscriptions) != 0:
		print "User Is already subscribed"
		ip = None
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404

	form = SubForm(request.POST or None, request.FILES or None) #For New Subscriptions!
	collection_of_fields = request.POST
	if request.method == "POST" and ip != None:
		if form.is_valid() and form.is_bound:
			newsub = form.save(commit=False)
			newsub.ipadd = ip
			newsub.save()
			send_to_user = SendMailTo(newsub.email, './newMember.txt')
			send_to_user.sendmail("newmember", "\'SpencerTech Members Attention!\'", "cat")
			messages.success(request, "Thank you {name} for signing up and becoming an independent member!".format(name=newsub.name))
			return HttpResponseRedirect(instance.get_absolute_url())
		else:
			messages.error(request, "Sorry, something wrong happened, I'll try and fix it, I'm a plumber when it comes to this. I fix everything bruh, everything")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print "Nothing to see here"

	share_string = quote_plus(instance.content)
	time_of_post = str(instance.readtime).split(":")
	if math.floor(float(time_of_post[0])) <= 0:
		timeshare = int(math.floor(60 * float(time_of_post[0]) + float(time_of_post[1])))
	elif float(time_of_post[1]) < 0:
		timeshare = "less than one minute"
	else:
		timeshare = int(math.floor(float(time_of_post[1])))

	context = {
		"instance": instance,
		"title": instance.title,
		"share_string": share_string,
		"has_image": instance.image.__bool__(),
		"timeshare": str(timeshare),
		"proxy_detail": re.match("^(/posts/){1}(\w+\-?)+/$", str(request.path)),
		"form": form,
		"methods": methods,
		"ipadd": ip,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active() #.order_by("-timestamp")
	json_script = urlopen("http://api.wunderground.com/api/c88441dcb4b52c50/geolookup/q/autoip.json").read()
	json_dict = json.loads(json_script)
	location = json_dict['location']
	latitude = location['lat']
	longitude = location['lon']
	latitude = location['lat']
	wui = location["wuiurl"]
	
	if request.user.is_staff:
		queryset_list = Post.objects.all()
	
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 8) # Show 8 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"object_list": queryset, 
		"title": "List",
		"page_request_var": page_request_var,
		"today": today,
		"proxy_list": re.match("(/posts/)", str(request.path)),
		"post_cutoff": str(request.path),
		"weather": location, #location of users temperature
		"wui": wui,
		"latitude": location["lat"],
		"longitude": location["lon"],
	}

	return render(request, "post_list.html", context)

def post_update(request, slug=None):
	if not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		try:
		
			if instance.image.width > 1200 or instance.image.height > 630:
				messages.error(request, "%s  violates image upload constraints"%(instance.image.name))
				return HttpResponseRedirect("/posts/create")
			
			else:
				#change the state of the share grid for post
				# message success
				instance.save()
				messages.success(request, "Successfully Created")
				return HttpResponseRedirect(instance.get_absolute_url())
		except ValueError:
			#Perform your logic with the image attribute `blank`
			instance.save()
			messages.success(request, "Successfully Created")
			return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}

	return render(request, "post_form.html", context)



def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return HttpResponseRedirect("/posts/")
