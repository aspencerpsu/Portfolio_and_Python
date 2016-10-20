try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass

import math
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# from comments.models import *

from .forms import PostForm
from .models import Post
from .utils import *

# Create your views here.
def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
		
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		if instance.image.url:
			instance.share = '<meta property="og:image" content="/static/img/%s"'%instance.image.url
		instance.save()
		else:
			instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content)
	# comments = Comment.objects.filter_by_instance(instance)
	time_of_post = str(instance.readtime).split(":")
	if math.floor(float(time_of_post[0])):
		timeshare = int(math.floor(60* float(time_of_post[0]) + float(time_of_post[1])))
	elif float(time_of_post[1]) < 0:
		timeshare = "less than one minute"
	else:
		timeshare = int(math.floor(float(time_of_post[1])))

	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
		# "comments": comments,
		"timeshare": str(timeshare),
		"proxy_detail": re.match("^(/posts/){1}(\w+\-?)+/$", str(request.path)),
	}

	return render(request, "post_detail.html", context)

def post_list(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active() #.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
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
	}
	return render(request, "post_list.html", context)

def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
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
	return redirect("posts:list")
