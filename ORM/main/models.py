from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=2064)
    contant = models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateTimeField()
    # late_update = models.DateTimeField(default=publish_date)