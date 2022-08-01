web: daphne chat_app.asgi:application --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker --settings=chat_app.settings -v2