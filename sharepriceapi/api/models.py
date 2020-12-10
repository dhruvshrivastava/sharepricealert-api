from django.db import models

class Watchlist(models.Model):
    created_by = models.ForeignKey('auth.User', related_name='watchlist', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.created_by)


class Ticker(models.Model):
    ticker_name = models.CharField(max_length=50)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.ticker_name)




