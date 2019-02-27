from django.db import models
from django.utils import timezone
# Create your models
# title
# text
# created_date (should be populated with current dat/time when record created)
# published_date (should be populated when record created and if updated)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    published_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title