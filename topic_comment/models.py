from django.db import models
from django.contrib.auth.models import User
from  django.utils import timezone
from django.urls import reverse
#from ckeditor.fields import RichTextField
# Create your models here.

class Topic(models.Model):
	user       = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE  )
	title      = models.CharField(max_length=100)
	content    = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now=True)
	update_at  = models.DateTimeField(auto_now_add=True)
	like       = models.ManyToManyField(User,default=None,blank=True,)
	image      = models.ImageField(upload_to='imageTopic/',null=True)
	def get_absolute_url(self):
		return reverse('topic_comment:topic_details', kwargs={'id':self.id})
		 

	def __str__(self):
		return self.title

class Comments(models.Model):
	user        = models.ForeignKey(User, related_name='userComment', on_delete=models.CASCADE,blank=True,null=True  )
	topic       = models.ForeignKey('Topic', related_name='Comments_Topic', on_delete=models.CASCADE  )
	comments    = models.TextField(blank=True, null=True)
	created_at  = models.DateTimeField(default=timezone.now)
	parent      = models.ForeignKey('self',related_name='replies',blank=True,on_delete=models.CASCADE,null=True )
	update_at   = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)