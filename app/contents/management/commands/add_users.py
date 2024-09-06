import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

            
class Command(BaseCommand):
    help = 'Add users'

    def handle(self, *args, **options):
        
        superuser_data = {
                     'username' : os.environ.get("SUPERUSER"),
                     'password' : os.environ.get("SUPERUSER_PASS"),
                    }
        user_data = {
                'username' : os.environ.get("USER"),
                'password' : os.environ.get("USER_PASS"),
               }

        superuser = User.objects.filter(username=superuser_data['username']).first()
        if not superuser:
            User.objects.create_superuser(username=superuser_data['username'], password=superuser_data['password'], email='')

        user = User.objects.filter(username=user_data['username']).first()
        if not user:
            User.objects.create_user(username=user_data['username'], password=user_data['password'], email='')
        
