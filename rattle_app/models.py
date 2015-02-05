from django.db import models
from django.contrib.auth.models import User
import hashlib

# Create your models here.
class Rattle(models.Model):
    content = models.CharField(max_length=140)
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True, blank=True)
 
 
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
 
    def gravatar_url(self):
        return "static/gfx/Skeleton-icon.png"
 
 
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])