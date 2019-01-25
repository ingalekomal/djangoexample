from django.db import models

# Create your models here.

class AddStud1(models.Model):
    def __str__(self):
        return self.name
