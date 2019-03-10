import requests

from .utils import to_slug, new_uuid

class Post:
    def __init__(self, title, uri=None, description=None):
        self.title = title
        self.uuid = new_uuid()
        self.uri = uri
        self.description = description
        self.meta = {}

    @property
    def slug(self):
        return to_slug(title)

    