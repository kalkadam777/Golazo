from django.db import models

class LiveBroadcast(models.Model): 
    name = models.CharField(max_length=150) 
    url = models.TextField(max_length=1000) 
     
    def __str__(self): 
        return f"{self.name} - {self.url}"   
 
    class Meta: 
        verbose_name = 'LiveBroadcast' 
        verbose_name_plural = 'LiveBroadcasts'
