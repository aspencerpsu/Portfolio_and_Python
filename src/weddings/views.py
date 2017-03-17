from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def wedding_create(request):
  if request.method == "GET":  
    form = WeddingForm()
  if request.method == "POST":
    form = WeddingForm(request.POST, request.FILES)
    if form.is_valid() and form.is_bound:
      form.save(commit=True)
      messages.success(request, "Successfully created your bio, bless up!")
      return HttpResponseRedirect("/thebigday")
    else:
      form = WeddingForm()
      context = {'form': form}
      messages.error(request, "Sorry somthing's wrong")
      return render(request, 'wedding_form.html', context) 

  context = {'form': form}
  return render(request, "wedding_form.html", context)
