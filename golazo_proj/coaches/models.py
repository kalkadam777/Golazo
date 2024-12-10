from django.db import models
from clubs.models import Club
from django_countries.fields import CountryField

class Manager(models.Model):
    name = models.CharField(max_length=100)
    current_club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name='managers')
    country = CountryField(default='ES')
    age = models.IntegerField()
    photo = models.ImageField(upload_to='manager_photos/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.current_club})"

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'
    
    
class ManagingHistory(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='managing_history')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='managing_history')
    transfer_date = models.DateField()

    def __str__(self):
        return f"Transfer of {self.manager.name} to {self.club.name} on {self.transfer_date}"

    class Meta:
        verbose_name = 'Managing History'
        verbose_name_plural = 'Managing Histories'
    
     
    
    
