from django.db import models
from django.contrib.auth import get_user_model 

User = get_user_model()


class Ticker(models.Model):
    ticker_name = models.CharField(max_length=50)
    def __str__(self):
        return self.ticker_name


class Watchlist(models.Model):
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    tickers = models.ManyToManyField(Ticker)

