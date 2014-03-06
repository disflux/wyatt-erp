from django.db import models

class Report(models.Model):
    lot_number = models.CharField(max_length=16)