from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from accounts.serializers import UserSerializers
from utils.responses import HTTP_200, HTTP_400

from django.shortcuts import render

# Create your views here.
from accounts.views import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from utils.responses import *
from django.contrib.auth import authenticate, logout, login
from member.models import Member
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from organization.models import Role
from utils.utils import generate_otp, generate_unique_code
from organization.models import *
from member.serializers import MemberValidationSerializer
from utils.email_function import send_self_registration_verification


class LoginAPI(APIView):
    """
    Handle api for login

    """

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["username", "password"],
            properties={
                "username": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Username of the user.",
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Password of the user.",
                ),
            },
        ),
        response_schema={
            "200": openapi.Response(
                description="API returns success message.",
                examples={
                    "application/json": {
                        "message": [],
                        "status": "success",
                    }
                },
            ),
            "400": openapi.Response(
                description="Data required or Integrity errors.",
                examples={
                    "application/json": {
                        "error": {
                            "username": [],
                            "email": [],
                            "user": [],
                            "member": [],
                            "non_field_error": [],
                        },
                        "status": "failed",
                    }
                },
            ),
        },
    )
    def post(self, request, *args, **kwargs):
        """
        # Handle post request for login.

        * Body params : Provide username/email and password.

        * Path params : NA.

        * Query params : NA.

        * Return : A HTTP response of success of failure message as json data.

        """

        username = request.data.get("username")
        password = request.data.get("password")

        if not username:
            return HTTP_400(error={"username": ["username is required"]})
        if not isinstance(username, str):
            return HTTP_400(error={"username": ["username must be a string"]})

        if not password:
            return HTTP_400(error={"password": ["password is required"]})
        if not isinstance(password, str):
            return HTTP_400(error={"password": ["password must be a string"]})

        try:
            user_instance = User.objects.get(username=username)
        except User.DoesNotExist:
            return HTTP_404(error={"username": ["User with username does not exist."]})

        if user_instance.is_active is False:
            return HTTP_403(
                error={
                    "username": ["User is inactive. reset password or contact admin."]
                }
            )

        try:
            member_instance = Member.objects.get(user=user_instance)
        except Member.DoesNotExist:
            return HTTP_404(error={"member": ["Member does not exist."]})

        if member_instance.is_invited is True:
            return HTTP_403(error={"member": ["Member is invited but not confirmed."]})

        if member_instance.is_active is False:
            return HTTP_403(
                error={
                    "member": ["Member is inactive. reset password or contact admin."]
                }
            )

        user = authenticate(request=request, username=username, password=password)

        if not user:
            return HTTP_401(
                error={"non_binary_error": ["Invalid username or password"]}
            )

        login(request, user)

        print(f"user +++++++++++++++++++++++++++++++++++ {user}")
        return HTTP_200(message={"message": "Logged in successfully"})


class LogoutAPI(APIView):
    """
    Logout API
    """

    def post(self, request):
        """
        # Handle POST request to logout.

        * Body params : NA.
        * Response : HTTP_200
        """
        logout(request)
        return HTTP_200(message={"message": "Logged out successfully"})


class OTPVerifyMemberAPI(APIView):
    """
    Verify a member using token sent via email.

    """

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["email", "otp"],
            properties={
                "email": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="email of the user.",
                ),
                "otp": openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="OTP which has send to the user's mail.",
                ),
            },
        ),
        response_schema={
            "200": openapi.Response(
                description="API returns success message.",
                examples={
                    "application/json": {
                        "message": [],
                        "status": "success",
                    }
                },
            ),
            "400": openapi.Response(
                description="Data required or Integrity errors.",
                examples={
                    "application/json": {
                        "error": {
                            "username": [],
                            "email": [],
                            "user": [],
                            "member": [],
                            "otp": [],
                            "non_field_error": [],
                        },
                        "status": "failed",
                    }
                },
            ),
        },
    )
    def post(self, request, *args, **kwargs):
        """
        # Handle POST request to verify otp.

        *  Path params : NA.

        *  body params : Provide otp and email address to verify email.

        *  Query params : NA.

        *  Return : A HTTP response with success or failure message as json data.

        """

        email = request.data.get("email")
        if not email:
            return HTTP_400(error={"email": ["email is required"]})

        if not isinstance(email, str):
            return HTTP_400(error={"email": ["email must be a string"]})

        otp = request.data.get("otp")
        if not otp:
            return HTTP_400(error={"otp": ["otp is required"]})

        if not isinstance(otp, int):
            return HTTP_400(error={"otp": ["otp must be an integer"]})

        try:
            user_instance = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            return HTTP_404(error={"email": ["User with this email does not exist"]})
        try:
            member_instance = Member.objects.get(user=user_instance)
        except Member.DoesNotExist:
            return HTTP_404(error={"email": ["Member with this email does not exist"]})

        valid_otp = member_instance.otp

        if valid_otp == otp:
            member_instance.is_invited = False
            member_instance.save()
            return HTTP_200({"message": "OTP verified successfully"})

        return HTTP_400(error={"otp": ["Invalid OTP or incorrect otp"]})


# from django.http import JsonResponse
# from django.middleware.csrf import get_token

# def csrf_token(request):
#     return JsonResponse({'csrfToken': get_token(request)})


class RegisterAPI(APIView):
    """
    Register a new user.
    """

    def post(self, request, *args, **kwargs):
        """
        # Handle POST request to create user and member.

        * Path params : NA.

        * Query params : NA.

        * Body params : email, password, name, phone, address, city, state, country.

        * Response : HTTP_200, HTTP_400, HTTP_404.

        """
        email = request.data.get("email")
        name = request.data.get("name")
        phone = request.data.get("phone_number")
        username = request.data.get("username")

        if not email:
            return HTTP_400(error={"email": ["This field is required."]})
        if not isinstance(email, str):
            return HTTP_400(error={"email": ["Invalid email,expected a string."]})

        email = User.objects.filter(email=email).exists()
       
        if email is True:
            return HTTP_400(error={"email": ["Email already exists."]})

        if not name:
            return HTTP_400(error={"name": ["This field is required."]})
        if not isinstance(name, str):
            return HTTP_400(error={"name": ["Invalid name,expected a string."]})

        if not username:
            return HTTP_400(error={"username": ["This field is required."]})
        if not isinstance(username, str):
            return HTTP_400(error={"username": ["Invalid username,expected a string."]})
        email = request.data.get("email")
        # username = 

        if not username.isalnum():
            return HTTP_400(
                error={
                    "username": [
                        "Invalid username,expected a string with alphanumeric characters."
                    ]
                }
            )
        organization_name = f"{name}" + "'s organization"

        organization_instance, created = Organization.objects.get_or_create(
            name=organization_name
        )
        if not created:
            return HTTP_400(
                error={
                    "organization": [
                        "Organization with name {} already exists.".format(
                            organization_name
                        )
                    ]
                }
            )

        user_instance = User.objects.create(
            first_name=name, username=username, email=email
        )
        role_instance, *_ = Role.objects.get_or_create(name="Admin")
        otp = generate_otp(6)
        invitation_code = generate_unique_code(6)

        request.data["user"] = user_instance.id
        request.data["organization"] = organization_instance.id
        request.data["role"] = role_instance.id
        request.data["otp"] = otp
        request.data["invitation_code"] = invitation_code
        request.data["is_active"] = True

        member_serializer = MemberValidationSerializer(data=request.data)
        if not member_serializer.is_valid():
            user_instance.delete()
            return HTTP_400(error=member_serializer.errors)
        member_serializer.save()
        email_send = send_self_registration_verification(request)
        if email_send is True:
            return HTTP_200(
                data={"message": "User created successfully,please verify your email."}
            )
        user_instance.delete()
        return HTTP_400(
            error={"email": ["Email sending failed, please try again later."]}
        )



#robinraphael440@gmail.com