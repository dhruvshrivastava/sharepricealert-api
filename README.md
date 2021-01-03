# sharepricealert-api
API built on Django Rest Framework and Celery which provides the following functionality:
- Add user's tickers to watchlist
- Send the user three types of alerts via E-mail: Frequency alerts, Percentage alerts and Volume alerts (explained below) 

# Frequency Alerts 
- The API sends the user periodic updates on his desired stocks. 

# Percentage Alerts
- The users can set a certain limit on the change percentage for a desired ticker, when the ticker exceeds that limit, the API sends an alert. 

# Volume Alerts
- The users can set a certain limit on the volume for a desired ticker, when the ticker exceeds that limit, the API sends an alert. 

# Installation & Usage 
- Install Celery=4.1.1, django-celery-beat and django-rest-framework
- Make sure that you set your Email Address and Password as environment variables for Python's smptb module. (I have used python-decouple to set my environment variables) 
- Peform migrations using python manage.py makemigrations, python manage.py migrate and python manage.py migrate --run-syncdb 
- Create the superuser using python manage.py createsuperuser
- Run the server: python manage.py runserver 
- Run the celery worker in a seperate process: celery -A sharepricealert worker --loglevel=info
- Run the celery scheduler in a seperate process: celery -A sharepricealert beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
- Go to 127.0.0.1:8000 to access the DRF's built in browsable API to set alerts and add tickers to your watchlist 
- Go to 127.0.0.1:8000/admin to schedule periodic tasks (sending alerts) using the Admin interface. *Set the interval for 1 minute or less*
 
