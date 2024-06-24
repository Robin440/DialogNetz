from django.shortcuts import render

# Create your views here.
from accounts.views import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from utils.responses import *
from django.contrib.auth import authenticate, logout, login


class LoginAPI(APIView):
    """
    Handle api for login

    """
    def post(self,request,*args,**kwargs):
        """
        # Handle post request for login.

        * Body params : Provide username/email and password.

        * Path params : NA.

        * Query params : NA.

        * Return : A HTTP response of success of failure message as json data.

        """

        username = request.data.get('username')
        password = request.data.get('password')

        if not username:
            return HTTP_400(error={"username":["username is required"]})
        if not isinstance(username,str):
            return HTTP_400(error={"username":["username must be a string"]})
        
        if not password:
            return HTTP_400(error={"password":["password is required"]})
        if not isinstance(password,str):
            return HTTP_400(error={"password":["password must be a string"]})
        
        user = authenticate(request=request,username=username,password=password)

        if not user:
            return HTTP_401(error={"username or password":["Invalid username or password"]})
        
        login(request,user)
        return HTTP_200(message={"message":"Logged in successfully"})
        