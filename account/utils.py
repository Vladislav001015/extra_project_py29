from django.core.mail import send_mail


def send_activation_code(code, email):
    send_mail(
        'Py29',
        f'Привет перейди по ссылке для активации аккаунта:\n\n localhost:8000/api/v1/account/activate/{code}',
        'sayansenedwne@gmail.com',
        [email]
    )
