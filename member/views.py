from django.shortcuts import render

# Create your views here.
from accounts.views import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from accounts.serializers import UserValidationSerializers
from utils.responses import *
from django.contrib.auth import authenticate, logout, login
from member.serializers import *
from utils.email_function import *

from utils.utils import *
from rest_framework.permissions import IsAuthenticated


class MemberCreateListAPI(APIView):
    """
    Handle create and list api

    """

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
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
            return HTTP_400(error={"member": ["Member not found."]})

        organization = get_member_organization(member)
        if not organization:
            return HTTP_400(error={"organization": ["Organization not found."]})

        if is_admin(member) is False:
            return HTTP_403(
                error={"permission": ["You don't have permission to access this."]}
            )

        member_instances = Member.objects.filter(organization=organization)

        member_serializer = MemberSerializer(member_instances, many=True)

        return HTTP_200(data=member_serializer.data)

    def post(self, request, *args, **kwargs):
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
            return HTTP_400(error={"member": ["Member not found."]})

        if is_admin(member) is False:
            return HTTP_403(
                error={"permission": ["You don't have permission to access this."]}
            )

        organization = get_member_organization(member)
        if not organization:
            return HTTP_400(error={"organization": ["Organization not found."]})

        password = request.data.get("password")
        confirm_password = request.data.get("confirm_password")
        username = request.data.get("username")
        email = request.data.get("email")
        name = request.data.get("first_name")
        role = request.data.get("role")
        roles = ["Admin", "Member"]

        if not password:
            password = None
        if not role:
            return HTTP_400(error={"role": ["This field is required."]})

        if not role in roles:
            return HTTP_400(
                error={"role": ["Invalid role. Please choose from Admin or Member."]}
            )

        try:
            role = Role.objects.get(name=role)
        except Role.DoesNotExist:
            return HTTP_400(
                error={"role": ["Role not found.Please contact the admin."]}
            )

        try:
            user_instance = User.objects.create(
                username=username, first_name=name, email=email
            )
            user_instance.set_password(password)
            user_instance.save()

        except Exception as e:
            return HTTP_400(
                error={
                    "user": [f"Failed to create user or {e}. Please contact the admin."]
                }
            )

        

        otp=generate_otp(length=6)
        invitation_code =generate_unique_code(length=6)
        

        request.data["user"] = user_instance.id
        request.data["organization"] = organization.id
        request.data["role"] = role.id
        request.data["name"] = name
        request.data['otp']=otp
        request.data['invitation_code'] = invitation_code
        member_serializer = MemberValidationSerializer(data=request.data)
        if not member_serializer.is_valid():
            user_instance.delete()
            return HTTP_400(error=member_serializer.errors)
        
        email_send = send_invitation_email(request)

        if email_send is False:
            user_instance.delete()
            return HTTP_400(error={"email": ["Failed to send email. Please try again."]})
        member_serializer.save()

        return HTTP_201(message={"member": ["Member has created successfully."]})
