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

