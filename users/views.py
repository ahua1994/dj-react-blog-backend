from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from .serializers import *
# from .signals import *
from .models import *

# Create your views here.


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        token = Token.objects.create(user=user)

        data = {}

        data['key'] = token.key
        data['user'] = serializer.data

        headers = self.get_success_headers(data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(["POST"])
def logout_view(request):
    if request.user != "Anonymous User":
        request.user.auth_token.delete()
        return Response({"message": "You have been logged out"})
    return Response({"message": "You are not logged in"})
