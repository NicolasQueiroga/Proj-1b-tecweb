from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField('Tag', through="Tagging")

    def __str__(self):
        s = (f'{self.id}. {self.title}')
        return s

class Tagging(models.Model):
    notes = models.ForeignKey('Note', on_delete=models.CASCADE)
    taggings = models.ForeignKey('Tag', on_delete=models.CASCADE)

class Tag(models.Model):
    tag_name = models.CharField(max_length=200)

    def __str__(self):
        s = (f'{self.id}. {self.tag_name}')
        return s
