from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    title = models.TextField()
    text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()

    def __unicode__(self):
        return self.title
