from celery import shared_task 
from .models import FrequencyAlerts
import datetime


@shared_task
def frequency_alerts():
    freq_alert = FrequencyAlerts.objects.all()
    now = datetime.datetime.utcnow()
    for alert in freq_alert:
      time_after_interval = alert.time_set + datetime.timedelta(minutes=int(alert.interval))
      if now.hour == alert.time_set.hour and now.minute == alert.time_set.minute: 
         print("Frequency Alert is being sent")
         FrequencyAlerts.objects.filter(pk=alert.id).update(time_set=time_after_interval)
      else:
          print(now)
          print(alert)