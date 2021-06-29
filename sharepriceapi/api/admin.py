from django.contrib import admin
from .models import Ticker, TickerList

admin.site.register(Ticker)
admin.site.register(TickerList)