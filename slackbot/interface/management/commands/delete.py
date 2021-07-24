from django.core.management.base import BaseCommand, CommandError
from interface.models import Posts, SlackBots


class Command(BaseCommand):
    help = 'Удаление всех ботов'

    def handle(self, *args, **options):
        Posts.objects.all().delete()
        SlackBots.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news'))  
