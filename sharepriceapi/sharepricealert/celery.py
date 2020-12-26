import os
from celery import Celery 
from celery.schedules import crontab
from django.conf import settings



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sharepricealert.settings')

app = Celery('sharepricealert')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, frequency_alerts())
    sender.add_periodic_task(30.0, test.s('world'), expires=10)
    
@app.task
def test(arg):
  print(arg)
    
    

    
