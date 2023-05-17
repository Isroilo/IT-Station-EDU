from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from main.models import *


@api_view(['POST'])
def signin_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        usrs = User.objects.get(username=username)
        usr = authenticate(username=username, password=password)
        try:
            if usr is not None:
                status = 200
                token, created = Token.objects.get_or_create(user=usrs)
                data = {
                    'username': username,
                    'user_id': usrs.id,
                    'token': token.key,
                }
            else:
                status = 403
                message = " Username yoki parol noto'g'ri ! "
                data = {
                    'status': status,
                    'message': message,
                }
        except User.DoesNotExist:
            status = 404
            message = ' Bunday foydalanuvchi mavjud emas! '
            data = {
                'status': status,
                'message': message,
            }
        return Response(data)
    except Exception as err:
        return Response(f'{err}')


@api_view(['POST'])
def signup_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User.objects.create_user(username=username, password=password)
    ser = UserSerializer(user)
    return Response(ser.data)


def logout_view(request):
    logout(request)
    return Response("logout")