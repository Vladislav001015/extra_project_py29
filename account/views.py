from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from account.serializers import *

User = get_user_model()


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            'Вы успешно зарегистровались. Вам отправлено письмо на почту с активацией',
            status=201
            )


class ActivationAPIView(APIView):

    def get(self, request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save(update_fields=['is_active', 'activation_code'])
        return Response('Успешно', status=200)


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializers = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializers.is_valid(raise_exception=True)
        serializers.set_new_password()
        return Response('Пароль изменен')


class ForgotPasswordAPIView(APIView):
    def post(self, request):
        ...
        # запрашиваем email, проверяем есть ли такой пользователь, генерируем код и отправлем его ему на почту

class ForgotPasswordConfirmAPIView(APIView):
    def post(self, request):
        ...
        # запрашиваем почту, код, пароль1, пароль2, проверям есть ли такой пользователь, проверяем код относится к нему или нет, проверяем пароли, -> меняем пароль