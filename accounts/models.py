from django.db import models
from django.contrib.auth.models import User
from  django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    
    user        = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE  )
    bio         = models.TextField(max_length=1000)
    image       = models.ImageField(upload_to='post/')
    phon_number = models.CharField(max_length=15,null=True)
    created_at  = models.DateTimeField(auto_now=True) 
    update_at   = models.DateTimeField(auto_now_add=True)
    slug        = models.SlugField(null=True,blank=True)
     
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)
   
    @property
    def image_url(self):
    	if self.image and hasattr(self.image, 'url'):
    		return self.image.url
  

    def __str__(self):
        return '%s' %(self.user)

@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)