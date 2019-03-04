from django.db import models
from django.utils import timezone


class Conference(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    participants_number = models.IntegerField()
    place = models.CharField(max_length=100)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
