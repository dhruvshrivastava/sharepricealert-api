from django.db import models
from django.utils import timezone 

class Ticker(models.Model):
    ticker_name = models.CharField(max_length=100, unique=True)
    watchlist_of = models.ForeignKey('auth.User', related_name='watchlist', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.ticker_name)


class FrequencyAlerts(models.Model):
    
    alert_of = models.ForeignKey('auth.User', related_name='frequency_alerts', on_delete=models.CASCADE, null=True)
    time_set = models.DateTimeField(default=timezone.now())
    ticker = models.CharField(max_length=100, unique=True)
    interval = models.CharField(max_length=100)
    def __str__(self):
         template = '{0.ticker} {0.time_set} {0.interval}'
         return template.format(self)

class VolumeAlerts(models.Model):
  
    alert_of = models.ForeignKey('auth.User', related_name='volume_alerts', on_delete=models.CASCADE, null=True)
    ticker = models.CharField(max_length=100, unique=True)
    limit = models.CharField(max_length=100)
    def __str__(self):
         template = '{0.ticker} {0.limit}'
         return template.format(self)

class PercentageAlerts(models.Model):

    alert_of = models.ForeignKey('auth.User', related_name='percentage_alerts', on_delete=models.CASCADE, null=True)
    ticker = models.CharField(max_length=100, unique=True)
    limit = models.CharField(max_length=100)
    def __str__(self):
         template = '{0.ticker} {0.limit}'
         return template.format(self)






    
    