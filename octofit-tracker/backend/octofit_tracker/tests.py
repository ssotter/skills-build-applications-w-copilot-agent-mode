from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='T')
        user = User.objects.create_user(username='u', email='u@t.com', password='pw', team=team)
        self.assertEqual(user.email, 'u@t.com')
    def test_activity_create(self):
        team = Team.objects.create(name='T')
        user = User.objects.create_user(username='u', email='u@t.com', password='pw', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=10, distance=1.5)
        self.assertEqual(str(activity), 'u - run')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='T')
        lb = Leaderboard.objects.create(team=team, points=42)
        self.assertEqual(str(lb), 'T: 42')
    def test_workout_create(self):
        workout = Workout.objects.create(name='W', description='desc')
        self.assertEqual(str(workout), 'W')
