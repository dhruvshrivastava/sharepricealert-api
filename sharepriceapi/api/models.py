from django.db import models
import datetime

class Watchlist(models.Model):
    created_by = models.ForeignKey('auth.User', related_name='watchlist', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.id)


class Ticker(models.Model):
    ticker_name = models.CharField(max_length=100, unique=True)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.ticker_name)

class Alerts(models.Model):
    created_by = models.ForeignKey('auth.User', related_name='alerts', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.id)


class FrequencyAlerts(models.Model):
    alert = models.ForeignKey(Alerts, on_delete = models.CASCADE, null = True)
    time_set = models.DateTimeField(default=datetime.datetime.now())
    ticker = models.CharField(max_length=100, unique=True)
    interval = models.CharField(max_length=100)
    def __str__(self):
         template = '{0.ticker} {0.time_set} {0.interval}'
         return template.format(self)

class VolumeAlerts(models.Model):
    alert = models.ForeignKey(Alerts, on_delete = models.CASCADE, null = True)
    ticker = models.CharField(max_length=100, unique=True)
    limit = models.CharField(max_length=100)
    def __str__(self):
         template = '{0.ticker} {0.limit}'
         return template.format(self)

class PercentageAlerts(models.Model):
    alert = models.ForeignKey(Alerts, on_delete = models.CASCADE, null = True)
    ticker = models.CharField(max_length=100, unique=True)
    limit = models.CharField(max_length=100)
    def __str__(self):
         template = '{0.ticker} {0.limit}'
         return template.format(self)



    
    