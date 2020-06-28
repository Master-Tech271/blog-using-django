from django.db import models

# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.title
    
