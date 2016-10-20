from django.db import models
from datetime import date
from django.utils import timezone
from django.db.models.fields.files import FieldFile
from django.core.files import File
from django.contrib.sites.models import Site

def fileback(instance, filename):
	return "/weeklyProject/%Y/%m/{0}/".format(filename[filename.rfind(".") + 1:])

# Create your models here.
class Blogs(models.Model):

	filetype=models.CharField(max_length=5, unique=True)

	# def __init__(self):
	# 	self.filetype = filetype

	def __unicode__(self):
		return u"%s"%(self.filetype)

	topic=models.CharField(max_length=100)
	abstract=models.TextField(max_length=2000)
	datestamp=models.DateField(auto_now=False, auto_now_add=False,default=date.today)
	timestamp=models.TimeField(auto_now=False, auto_now_add=False, default=timezone.now)
	content=models.FileField(upload_to="/weeklyProject/%Y/%m/", max_length=100, )
	figures=models.ImageField(upload_to="/img", height_field=None, width_field=None, max_length=100)
	graphs=models.FileField(upload_to=fileback)
	census=models.IntegerField()

class Admin:
	pass
