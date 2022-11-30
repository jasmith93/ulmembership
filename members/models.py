from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField()
    is_member = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'