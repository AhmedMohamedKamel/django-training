from django.db import models

class Artist(models.Model):
    stageName = models.CharField(unique=True, blank=False, max_length=70, null=False)
    socialLink = models.URLField(max_length=200, blank = True)

    def __str__(self):
        return "Artist stageName is:" +self.stageName
    
    class Meta:
        db_table = 'artists'
        ordering = ['stageName']
