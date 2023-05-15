from django.db import models
from django.utils import timezone

# Create your models here.

class UserAudio(models.Model):
    timeStamp = models.DateTimeField()
    createdAt = models.DateTimeField(default=timezone.now)
    Audio_content = models.FileField(upload_to='audio/')
    Video_content = models.CharField(null= True, blank=True, default= None)
    Infant_cry_class_by_model = models.CharField(null=True, blank=True, default= None)
    Infant_cry_class_rate = models.CharField(null=True, blank=True, default= None)
    Infant_cry_class_by_user = models.CharField(null=True, blank=True, default= None)

    # from AudioIntelligeneceAPI
    class_distribution = models.CharField(null=True, blank=True, default= None)

    # data cache data
    solutions_executed = models.CharField(null=True, blank=True, default= None)
    user_solution = models.CharField(null=True, blank=True, default= None)

    # Solution to client app
    text = models.CharField(null=True, blank=True, default= None)
    solution_audio = models.CharField(null=True, blank=True, default= None)
    





