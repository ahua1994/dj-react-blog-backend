from django.shortcuts import render
from .models import *

# Create your views here.


class RegisterView():
    pass


# class LoginView(APIView):
#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']
#         # use a method to get access token (from the package you are using)
#         # access token class will return access token if the user is authenticated
#         # otherwise it will return error response
#         pass


class LogoutView():
    pass
