from django.db import models

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
    ticker = models.CharField(max_length=100, unique=True)
    interval = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return str(self.ticker), str(self.interval)

class VolumeAlerts(models.Model):
    alert = models.ForeignKey(Alerts, on_delete = models.CASCADE, null = True)
    ticker = models.CharField(max_length=100, unique=True)
    limit = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return str(self.ticker), str(self.limit)

class PercentageAlerts(models.Model):
    alert = models.ForeignKey(Alerts, on_delete = models.CASCADE, null = True)
    ticker = models.CharField(max_length=100, unique=True)
    limit = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return str(self.ticker), str(self.limit)



    
    