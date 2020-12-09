from django.db import models

class Ticker(models.Model):
    ticker_name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.ticker_name)


class Watchlist(models.Model):
    created_by = models.ForeignKey('auth.User', related_name='watchlist', on_delete=models.CASCADE, null=True)
    tickers = models.ManyToManyField(Ticker)
    def __str__(self):
        return str(self.tickers)

