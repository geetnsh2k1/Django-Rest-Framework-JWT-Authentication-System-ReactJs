from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from django.conf import settings

from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer

FALSE_RESPONSE = {"Status":False, "Result": "FAILED"}
TRUE_RESPONSE = {"Status":True, "Result": "SUCCESSFUL"}

INVALID_CREDENTIALS = {"Status":False, "Result": "INVALID CREDENTIALS RECIEVED!"}

import json

@api_view(['POST'])
def signup(request):
    result = {"Status": True}
    try:
        new_t = UserSerializer(data=request.data)
        if new_t.is_valid():
            new_t.save()
        else:
            result['Status'] = False
        
    except Exception as e:
        print(e)
        result['Status'] = False
    return Response(result)

@api_view(['GET'])
def logout(request):
    try:
        response = Response()
        response.delete_cookie('refresh_token')
        response.data = TRUE_RESPONSE
        return response
    except Exception as e:
        print(e)
        return Response(FALSE_RESPONSE)
    
# NEXT STEPS
# 1. Update user model to store access_token, refresh_token and expire date to check if token passed from request is validate token or not and also use it to generate new access_token 

from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['GET'])
def refresh(request):
    
    attrs = { "refresh": request.COOKIES['refresh_token']}
    
    refresh = RefreshToken(attrs['refresh'])

    data = {'access': str(refresh.access_token)}

    if api_settings.ROTATE_REFRESH_TOKENS:
        if api_settings.BLACKLIST_AFTER_ROTATION:
            try:
                # Attempt to blacklist the given refresh token
                refresh.blacklist()
            except AttributeError:
                # If blacklist app not installed, `blacklist` method will
                # not be present
                pass

        refresh.set_jti()
        refresh.set_exp()

        data['refresh'] = str(refresh)

    return Response(data)
    
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def google(request):
    return Response({"Status":True, "Google": "https://www.google.co.in/"})