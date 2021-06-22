from celery import shared_task 
from .models import FrequencyAlerts, PercentageAlerts, VolumeAlerts, TriggerAlerts
from .quotes import get_ticker_quote
from django.core.mail import send_mail
from decouple import config 
import datetime
import pytz

@shared_task
def frequency_alerts():
    freq_alert = FrequencyAlerts.objects.all()
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(tz)
    for alert in freq_alert:
      time_after_interval = alert.time_set + datetime.timedelta(minutes=int(alert.interval))
      if now.hour == time_after_interval.hour and now.minute == time_after_interval.minute: 
         data = get_ticker_quote(alert.ticker)
         price = str(data["price"].item())
         high = str(data["regularMarketDayHigh"].item())
         low = str(data["regularMarketDayLow"].item())
         message = 'Price: '  + price + ' ' + 'High: ' + high + ' ' 'Low: ' + low
         send_mail("Frequency Alert", message, config('EMAIL_HOST_USER'), [str(alert.alert_of.email)])
         print("Frequency Alert sent", alert.ticker)
         FrequencyAlerts.objects.filter(pk=alert.id).update(time_set=time_after_interval)
      else:
        print(time_after_interval)
        print(now)
      
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
    if int(volume) >= int(alert.limit):
      message = 'Your ticker has crossed the limit: ' + str(alert.limit)
      send_mail("Percentage Alert", message,config('EMAIL_HOST_USER'), [str(alert.alert_of.email)])
      print("Volume Alert sent ")
    else:
      print(alert)


@shared_task
def trigger_alerts():
  trigger_alert = TriggerAlerts.objects.all()
  for alert in trigger_alert:
    data = get_ticker_quote(alert.ticker)
    price = data["price"].item()
    blimit = alert.below_limit.replace(",","")
    alimit = alert.above_limit.replace(",","")
    if float(price) <= float(blimit) or float(price) >= float(alimit):
      message = "Alert has been triggered, current price: " + str(price)
      send_mail("Trigger Alert", message, config('EMAIL_HOST_USER'), [str(alert.alert_of.email)])
      print("Trigger Alert sent")
    else:
      print(alert)