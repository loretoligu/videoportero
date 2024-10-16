from django.db import models

# Create your models here.
from django.utils import timezone

class doorRelease(models.Model):
	recdate = models.DateTimeField(null=True, verbose_name="date")
	userid = models.CharField(null=True, blank=True, max_length=20, verbose_name="user")
	success = models.BooleanField(null=True, blank=True, verbose_name="success")

