from django import forms
from pagedown.widgets import PagedownWidget
from .models import *

class PostForm(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget(show_preview=False))
	publish = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
	  model = Post
	  fields = [
	  "title",
	  "description",
	  "content",
	  "image",
	  "draft",
        ]

class SubForm(forms.ModelForm):
  name = forms.CharField(max_length=200, label="Your Full or Partial Name")
  email = forms.EmailField(max_length=254, label="Your Email Address")
  ipadd = forms.GenericIPAddressField(label="IP Address")
  class Meta:
    model = SubscriptionList
    fields = [
              "ipadd",
              "name",
              "email",
            ]
