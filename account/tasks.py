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

@app.task
def send_activation_code(email, code):
    send_mail(
        'Extra theme py29',
        f'Перейдите по этой ссылке чтобы активировать аккаунт: \n\n http://localhost:8000/api/v1/account/activate/{code}',
        'vladislav001015@gmail.com',
        [email]
    )

@app.task
def send_forgot_password_code(email, code):
    send_mail(
        'Extra theme py29',
        f'Вот ваш код для востановления пароля, никому не показывайте его: {code}',
        'vladislav001015@gmail.com',
        [email]
    )


@app.task
def send_spam():
    
    send_mail(
        'Extra theme py29',
        f'Загляни на наш сайт!',
        'vladislav001015@gmail.com',
        ['vladislav001015@gmail.com']
    )