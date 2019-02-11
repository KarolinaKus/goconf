from django.db import models
from django.utils import timezone


class Conf(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    participants_number = models.IntegerField()
    place = models.CharField(max_length=100)
    published_post_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=200)

    def publish(self):
        self.published_post_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
