from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    title = models.TextField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()

    def __unicode__(self):
        return self.title
