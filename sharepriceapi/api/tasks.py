from celery import shared_task 
from .models import FrequencyAlerts, PercentageAlerts, VolumeAlerts
import datetime
from .quotes import get_ticker_quote


@shared_task
def frequency_alerts():
    freq_alert = FrequencyAlerts.objects.all()
    now = datetime.datetime.utcnow()
    for alert in freq_alert:
      time_after_interval = alert.time_set + datetime.timedelta(minutes=int(alert.interval))
      if now.hour == alert.time_set.hour and now.minute == alert.time_set.minute: 
         data = get_ticker_quote(alert.ticker)
         print("Frequency Alert: " data)
         FrequencyAlerts.objects.filter(pk=alert.id).update(time_set=time_after_interval)
      else:
          print(now)
          print(alert)

@shared_task
def percentage_alerts():
  percentage_alert = PercentageAlerts.objects.all()
  for alert in percentage_alert:
    data = get_ticker_quote(alert.ticker)
    if data['regularMarketChangePercent'] == alert.limit:
      print("Percentage Alert is being sent")
    else:
      print(alert)

@shared_task
def volume_alerts():
  volume_alert = VolumeAlerts.objects.all()
  for alert in volume_alert:
    data = get_ticker_quote(alert.ticker)
    if data['regularMarketVolume'] == alert.limit:
      print("Volume Alert is being sent ")
    else:
      print(alert)
