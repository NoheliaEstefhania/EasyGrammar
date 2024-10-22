from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description_english = models.TextField()
    description_spanish = models.TextField()

    def __str__(self):
        return self.title