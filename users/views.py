from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
# from .signals import *
from .models import *

# Create your views here.


class RegisterView():
    pass


@api_view(["POST"])
def logout_view(request):
    if request.user != "Anonymous User":
        request.user.auth_token.delete()
        return Response({"message": "You have been logged out"})
    return Response({"message": "You are not logged in"})
