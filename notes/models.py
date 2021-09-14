from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        s = (f'{self.id}. {self.title}')
        return s
    