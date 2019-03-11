from django.core.management.base import BaseCommand, CommandError
from core.models import Post

from requests_html import HTMLSession


requests_html = HTMLSession()


def get_hn(filter="py"):
    r = requests_html.get('https://news.ycombinator.com/')
    pass


def get_reddit():
    pass


class Command(BaseCommand):
    help = 'Import content from known sites.'

    def add_arguments(self, parser):
        parser.add_argument('--hn', action='store_true')
        parser.add_argument('--reddit', action='store_true')
        # parser.add_argument('--pycoders', action='store_true')

    def handle(self, *args, **options):
        if options['hn']:
            get_hn()

        if options['reddit']:
            get_reddit()
