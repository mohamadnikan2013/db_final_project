from django.db import models


# Create your models here.

class App(models.Model):
    name = models.CharField(max_length=150, blank=True)
    # owner = models.OneToOneField('accounts.Member', related_name="store")
    # address = models.TextField(blank=True)
    # email = models.EmailField(blank=True)
    # mobile_phone = models.CharField(max_length=30, validators=[mobile_regex], blank=True)
    # description = models.TextField(blank=True)
