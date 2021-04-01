from django.core.management.base import BaseCommand
import time


class Command(BaseCommand):
    help = 'hello'

    def handle(self, *args, **options):
        time.sleep(10)
        print("Hello, world!")