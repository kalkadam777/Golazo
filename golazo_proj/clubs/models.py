from django.db import models
from django_countries.fields import CountryField

class Club(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    country = CountryField()  
    emblem = models.ImageField(upload_to='club_emblems/', null=True, blank=True)  
    league = models.CharField(max_length=100, default='Unknown League')

    def __str__(self):
        return f"{self.name} - {self.league}"  

    class Meta:
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'