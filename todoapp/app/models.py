from django.db import models

# Create your models here.

choose = (
    ('high','High'),
    ('medium', 'MEDIUM'),
    ('low','LOW'),
)


class Mod(models.Model):
    name = models.CharField(max_length=25, null=True)
    description = models.CharField(max_length=25, null=True)
    priority = models.CharField(max_length=6,choices=choose, null=True)
    date = models.DateField()
