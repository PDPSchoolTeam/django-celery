import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

app = Celery('root')

# Konfiguratsiyani django settings.py dan olib kelish # noqa
app.config_from_object('django.conf:settings', namespace='CELERY')

# Avtomatik tasklarni topish # noqa
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# quotes = [
#     "💪 Bugun kuchli bo‘l, ertangi kun g‘alaba sen bilan!", # noqa
#     "🚀 Harakat qilgan odam, oxir-oqibat muvaffaqiyatga erishadi!", # noqa
#     "🌟 Orzularingiz uchun kurashing, siz bunga loyiqsiz!", # noqa
#     "🔥 Har kun — yangi imkoniyat. Qani boshladik!", # noqa
#     "🎯 Maqsadingiz yo‘lidagi har bir qadam — g‘alabaga yaqinlashishdir!" # noqa
# ]

# @app.task
# def send(user_id: int):
#     import requests
#     import random
#     token = "your token"
#     message = random.choice(quotes)
#     url = f"https://api.telegram.org/bot{token}/sendMessage"
#     data = {
#         "chat_id": user_id,
#         "text": message,
#     }
#     response = requests.post(url, data=data)
#     return response.status_code

    # docker run -p 6379:6379 --name some-redis -d redis
    # celery -A root worker --loglevel=info
    # celery -A root.celery.app flower --port=5001
    # python manage.py shell
    # from root.celery import send
    # task = send.delay(tg_id)
    # print(task.id)
    # print(task.status)
    # print(task.state)
    # https://testdriven.io/courses/django-celery/getting-started/
