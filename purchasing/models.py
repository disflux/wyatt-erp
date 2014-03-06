from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=32)
