from django.db import models

# Create your models here.
# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    introduction = models.TextField()
    image = models.CharField(max_length=100)
    
    # returns name/title of object instead of 'object (#)'
    def __str__(self):
        return self.title #or self.title for blog posts