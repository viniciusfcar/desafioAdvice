from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        admin = User.objects.get(username='admin')
        
        if not admin:
            admin = User.objects.create_superuser(email='admin@gmail.com', username='admin', password='admin')