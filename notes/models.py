from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ForeignKey('Tag', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        s = (f'{self.id}. {self.title}')
        return s


class Tag(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, default='#ead3a7')

    def __str__(self):
        return self.name
