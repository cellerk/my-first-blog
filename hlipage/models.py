from django.db import models
from django.conf import settings

class Input(models.Model):
    #min_date = models.DateTimeField(blank=True, null=True)
    #max_date = models.DateTimeField(blank=True, null=True)

    min_date = models.DateField(blank=True, null=True)
    max_date = models.DateField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.min_date