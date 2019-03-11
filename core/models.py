import uuid

from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator
from taggit.managers import TaggableManager


class Post(models.Model):
    """A Post, posted on the site."""
    title = models.TextField()
    text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()
    uri = models.URLField()
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    published = models.BooleanField(editable=True, default=False)

    def __unicode__(self):
        return self.title
