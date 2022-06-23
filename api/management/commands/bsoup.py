from __future__ import absolute_import, unicode_literals
from django.core.management.base import BaseCommand
from api.tasks import bsoup


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        bsoup.delay()