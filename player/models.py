from typing_extensions import Required
from django.db import models

# Create your models here.


class T20Players(models.Model):

    ROLE_CHOICES = (
        ('Right Handed Batter', 'Right Handed Batter'),
        ('Left Handed Batter', 'Left Handed Batter'),
        ('All-Rounder', 'All-Rounder'),
        ('Right Arm Fast Bowler', 'Right Arm Fast Bowler'),
        ('Left Arm Fast Bowler', 'Left Arm Fast Bowler'),
        ('Right Arm Off Spinner', 'Right Arm Off Spinner'),
        ('Left Arm Off Spinner', 'Left Arm Off Spinner'),
        ('Leg Spinner', 'Leg Spinner'),

    )

    name = models.CharField(max_length=150, blank=False)
    age = models.IntegerField()
    date_of_birth = models.DateField(default='2001-01-01')
    height = models.DecimalField(decimal_places=2, max_digits=5)
    ranking = models.CharField(max_length=10, default='N/A')
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    title = models.CharField(max_length=50, default='N/A')
    image = models.TextField()
    bio = models.TextField(default='.')


class ODIPlayers(models.Model):
    ROLE_CHOICES = (
        ('Right Handed Batter', 'Right Handed Batter'),
        ('Left Handed Batter', 'Left Handed Batter'),
        ('All-Rounder', 'All-Rounder'),
        ('Right Arm Fast Bowler', 'Right Arm Fast Bowler'),
        ('Left Arm Fast Bowler', 'Left Arm Fast Bowler'),
        ('Right Arm Off Spinner', 'Right Arm Off Spinner'),
        ('Left Arm Off Spinner', 'Left Arm Off Spinner'),
        ('Leg Spinner', 'Leg Spinner'),

    )

    name = models.CharField(max_length=150, blank=False)
    age = models.IntegerField()
    date_of_birth = models.DateField(default='2001-01-01')
    height = models.DecimalField(decimal_places=2, max_digits=5)
    ranking = models.CharField(max_length=10, default='N/A')
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    title = models.CharField(max_length=50, blank=True)
    image = models.TextField()
    bio = models.TextField(default='.')


class TestPlayers(models.Model):

    ROLE_CHOICES = (
        ('Right Handed Batter', 'Right Handed Batter'),
        ('Left Handed Batter', 'Left Handed Batter'),
        ('All-Rounder', 'All-Rounder'),
        ('Right Arm Fast Bowler', 'Right Arm Fast Bowler'),
        ('Left Arm Fast Bowler', 'Left Arm Fast Bowler'),
        ('Right Arm Off Spinner', 'Right Arm Off Spinner'),
        ('Left Arm Off Spinner', 'Left Arm Off Spinner'),
        ('Leg Spinner', 'Leg Spinner'),

    )

    name = models.CharField(max_length=150, blank=False)
    age = models.IntegerField()
    date_of_birth = models.DateField(default='2001-01-01')
    height = models.DecimalField(decimal_places=2, max_digits=5)
    ranking = models.CharField(max_length=10, default='N/A')
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    title = models.CharField(max_length=50, blank=True)
    image = models.TextField()
    bio = models.TextField(default='.')
