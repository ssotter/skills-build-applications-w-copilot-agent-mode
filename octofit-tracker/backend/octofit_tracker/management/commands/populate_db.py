from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Limpa dados existentes
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Cria times
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Cria usuários super-heróis
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='123', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='123', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='123', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='123', team=dc),
        ]

        # Cria atividades
        for user in users:
            app_models.Activity.objects.create(user=user, type='run', duration=30, distance=5)

        # Cria leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=100)
        app_models.Leaderboard.objects.create(team=dc, points=80)

        # Cria workouts
        app_models.Workout.objects.create(name='Treino Marvel', description='Treino especial dos heróis Marvel')
        app_models.Workout.objects.create(name='Treino DC', description='Treino especial dos heróis DC')

        self.stdout.write(self.style.SUCCESS('Banco populado com dados de teste!'))
