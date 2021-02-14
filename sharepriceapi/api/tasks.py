from celery import shared_task 
from .models import FrequencyAlerts, PercentageAlerts, VolumeAlerts
from .quotes import get_ticker_quote
from django.core.mail import send_mail
from django.utils import timezone
from decouple import config 
import datetime

@shared_task
def print_test():
  freq_alert = FrequencyAlerts.objects.all()
  for alert in freq_alert:
    print(alert.alert_of.email)
  

@shared_task
def frequency_alerts():
    freq_alert = FrequencyAlerts.objects.all()
    now = timezone.now()
    for alert in freq_alert:
      time_after_interval = alert.time_set + datetime.timedelta(minutes=int(alert.interval))
      if now.hour == alert.time_set.hour and now.minute == alert.time_set.minute: 
         data = get_ticker_quote(alert.ticker)
         changePercent = str(data["regularMarketChangePercent"].item())
         price = str(data["price"].item())
         volume = str(data["regularMarketVolume"].item())
         high = str(data["regularMarketDayHigh"].item())
         low = str(data["regularMarketDayLow"].item())
         message = 'Price: '  + price + ' ' + 'High: ' + high + ' ' 'Low: ' + low
         send_mail("Frequency Alert", message, config('EMAIL_HOST_USER'), [str(alert.alert_of.email)])
         print("Frequency Alert sent", alert.ticker)
         FrequencyAlerts.objects.filter(pk=alert.id).update(time_set=time_after_interval)
      
@shared_task  
def percentage_alerts():
  percentage_alert = PercentageAlerts.objects.all()
  for alert in percentage_alert:
    data = get_ticker_quote(alert.ticker)
    changePercent = "{:.2f}".format(data["regularMarketChangePercent"].item())
    if changePercent >= alert.limit:
      message = 'Percentage Alert has been triggered for ' + str(alert.ticker)+ ',' + str(alert.limit)
      send_mail("Percentage Alert", message, config('EMAIL_HOST_USER'), [str(alert.alert_of.email)])
      print("Percentage Alert sent", alert.ticker)
    else:
      print(alert)

@shared_task
def volume_alerts():
  volume_alert = VolumeAlerts.objects.all()
  for alert in volume_alert:
    data = get_ticker_quote(alert.ticker)
    volume = data["regularMarketVolume"].item()
    if volume >= alert.limit:
      message = 'Your ticker has crossed the limit: ' + str(alert.limit)
      send_mail("Percentage Alert", message,config('EMAIL_HOST_USER'), [str(alert.alert_of.email)])
      print("Volume Alert sent ")
    else:
      print(alert)
