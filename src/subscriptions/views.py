from django.shortcuts import render, render_to_response
from django.contrib import messages

def subscription_create(request):
  if request.GET:
	full_path = request.get_full_path 
  form = SubForm(request.POST or None, request.FILES or None)
  
  if form.is_valid() or form.is_bound:
    form.save()
    messages.sucess(request, "Thanks for subscribing to station, 
				I'll give you more content with no ugly filler")
  else:
    messages.error(request, "Sorry, there was a problem handling request")
    return HttpResponseRedirect(full_path)
  context = {"form": form} 
  return render(request, "sub_form.html", context) 
