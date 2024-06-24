from django.shortcuts import render

# Create your views here.
from accounts.views import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from utils.responses import *
from django.contrib.auth import authenticate, logout, login
from member.serializers import *

from utils.utils import *
from rest_framework.permissions import IsAuthenticated



class MemberCreateListAPI(APIView):
    """
    Handle create and list api 

    """
    permission_classes = [IsAuthenticated]


    def get(self,request,*args,**kwargs):
        """
        Handle GET request to list all members according to the role.

        * Path params : NA.

        * Body params : NA.

        * Query params : Search params and filters.

        * Return : A HTTP response of member list as json.

        """

        user = request.user


        member = get_member(user)
        if not member:
            return HTTP_400(error={"member":["Member not found."]})
        
        organization = get_member_organization(member)
        if not organization:
            return HTTP_400(error={"organization":["Organization not found."]})
        
        
        if is_admin(member) is False:
            return HTTP_403(error={"permission":["You don't have permission to access this."]})
        
        member_instances = Member.objects.filter(organization=organization)



        member_serializer =MemberSerializer(member_instances,many=True)



        return HTTP_200(data=member_serializer.data)
    



    def post(self,request,*args,**kwargs):
        """
        # Handle POST request to create member.

        * Body params : Provide member details to create member and respective user as well.

        * Path params : NA.

        * Query params : NA.

        * Return : A HTTP response with success message or failed message.

        """
        
        user = request.user

        member = get_member(user)
        if not member:
            return HTTP_400(error={"member":["Member not found."]})
        
        if is_admin(member) is False:
            return HTTP_403(error={"permission":["You don't have permission to access this."]})
        
        organization = get_member_organization(member)
        if not organization:
            return HTTP_400(error={"organization":["Organization not found."]})
        
        




        