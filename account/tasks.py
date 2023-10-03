from django.core.mail import send_mail
from config.celery import app

@app.task
def send_test_message():
    import time

    time.sleep(30)
    
    send_mail(
        'Extra theme py29',
        f'Это тестовое сообщение',
        'vladislav001015@gmail.com',
        ['vladislav001015@gmail.com']
    )
