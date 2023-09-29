from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Extra theme py29',
        f'Перейдите по этой ссылке чтобы активировать аккаунт: \n\n http://localhost:8000/api/v1/account/activate/{code}',
        'vladislav001015@gmail.com',
        [email]
    )

def send_forgot_password_code(email, code):
    send_mail(
        'Extra theme py29',
        f'Вот ваш код для востановления пароля, никому не показывайте его: {code}',
        'vladislav001015@gmail.com',
        [email]
    )
