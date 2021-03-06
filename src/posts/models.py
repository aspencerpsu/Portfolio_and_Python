from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify

from .utils import *
#Create your models here.  


# MTV MODEL TEMPLATE VIEW

class PostManager(models.Manager):
	def active(self, *args, **kwargs):
		#Post.objects.all() = super(PostManager, self).all()
		return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

def upload_location(instance, filename):
	PostModel = instance.__class__
	new_id = PostModel.objects.order_by("id").last().id + 1
	return "%s/%s" %(instance.id, filename) 
	"""
	instance.__class__ gets the model Post. We must use this method because the model is defined below. 
	Then create a queryset ordered by the "id"s of each object, Then
		we get the last object in the queryset with the `.last()` method
	Which will give us the most recently created Model instance
	We add 1 to it, so we get what should be the same id as the post we are creating.

	"""

class Post(models.Model):

	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=120)
	description = models.CharField(max_length=120, default="None At The Moment")
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to=upload_location,
								null=True,
								blank=True,
								width_field="width_field",
								height_field="height_field")
	height_field=models.IntegerField(default=630, null=True, blank=True)
	width_field=models.IntegerField(default=1200, null=True, blank=True)	
	content=models.TextField()
	draft=models.BooleanField(default=False)
	publish=models.DateField(auto_now_add=True)
	readtime = models.TimeField(null=True)
	updated = models.TimeField(auto_now_add=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	objects = PostManager()

	def __unicode__(self):
		return u"{0}".format(self.title)

	def __str__(self):
		return "{0}".format(self.title)

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"slug":self.slug})

	class Meta:
		ordering = ["-timestamp", "-updated"]

	#def comment(self):
		#instance = self
		#qs = Comment.object.filter_by_instance(instance)
		#return qs

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)
	
	if instance.content:
		html_string = str(instance.content)
		read_time_var = get_read_time(html_string)
		instance.readtime = read_time_var
	
	if instance.image:
		instance.height_field = 630
		instance.image.width_field = 1200	

pre_save.connect(pre_save_post_receiver, sender=Post)
