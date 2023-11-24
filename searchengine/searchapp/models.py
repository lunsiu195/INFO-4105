from django.db import models

# Create your models here.

class CrawledPage(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=400)
    
    def __str__(self):
        return self.title
