from django.db import models

from django.db import models


class Character(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=100, null=False, blank= False)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    title = models.CharField(max_length=100)
    is_alive = models.BooleanField(default=True)
    description = models.TextField()
    seasons = models.JSONField(default=list)


    def __str__(self):
        return self.name


class House(models.Model):
    full_name = models.CharField(max_length=100)
    animal = models.CharField(max_length=30)
    region = models.CharField(max_length=100)
    year_of_foundation = models.PositiveIntegerField()
    lord = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, related_name='houses_lord')
    lady = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, related_name='houses_lady')
    number_of_members = models.PositiveIntegerField()
    motto = models.CharField(max_length=100)
    ancestral_weapon = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name