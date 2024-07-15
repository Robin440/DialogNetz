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
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import get_object_or_404
from django.db.models import Q

class ReceiveMessageAPI(APIView):
    """
    Receive message from sender
    """

    @swagger_auto_schema(
        responses={200: MessageSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        """
        # Handle GET request to list received messages for a specific receiver.

        * Path params : Provide id of receiver.
        * Body params : NA.
        * Query params : NA.
        * Return : A HTTP response of JSON format with data of received messages.
        """
        receiver_id = kwargs.get("receiver_id")
        if not receiver_id:
            return HTTP_400(error={"receiver_id": ["Please provide receiver id."]})

        receiver = get_object_or_404(Member, id=receiver_id)
        received_messages = Message.objects.filter(receiver=receiver)
        serializer = MessageSerializer(received_messages, many=True)
        return HTTP_200(data=serializer.data)

class SendMessageAPIView(APIView):
    """
    API view for send message
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200: MessageSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        """
        # Handle GET request to list sent messages for a specific sender.

        * Path params : Provide id of sender.
        * Body params : NA.
        * Query params : NA.
        * Return : A HTTP response of JSON format with data of sent messages.
        """
        sender_id = kwargs.get('sender_id')
        if not sender_id:
            return HTTP_400(error={"sender_id": ["Please provide sender id"]})

        sender = get_object_or_404(Member, id=sender_id)
        sent_messages = Message.objects.filter(sender=sender).order_by("timestamp")
        serializer = MessageSerializer(sent_messages, many=True)
        return HTTP_200(data=serializer.data)

    @swagger_auto_schema(
        request_body=MessageSerializer,
        responses={200: MessageSerializer,
                   400: "Error message"}
    )
    def post(self, request, *args, **kwargs):
        """
        # Handle POST request to send message.

        * Path params : NA.
        * Request body : Provide content, sender_id, and receiver_id.
        * Response : A HTTP response of success message or failure as JSON data.
        """
        user = request.user
        if isinstance(user, AnonymousUser):
            return HTTP_400(error={"user": ["Found as anonymousUser, login and try again."]})

        member = get_member(user)
        if not member:
            return HTTP_400(error={"member": ["Not a member, login and try again."]})

        organization = get_member_organization(member)
        if not organization:
            return HTTP_400(error={"organization": ["Not a member of any organization, login and try again."]})

        sender_id = request.data.get('sender')
        receiver_id = request.data.get('receiver')
        if not sender_id or not receiver_id:
            return HTTP_400(error={"sender": ["Please provide sender id"], "receiver": ["Please provide receiver id"]})

        request.data["sender"] = get_object_or_404(Member, id=sender_id).id
        request.data["receiver"] = get_object_or_404(Member, id=receiver_id).id

        serializer = MessageSerializer(data=request.data)
        if not serializer.is_valid():
            return HTTP_400(error={"non_binary_error": serializer.errors})

        serializer.save()
        return HTTP_200(data=serializer.data)
    

class ChatviewAPI(APIView):
    """
    # Handle POST request to get all messages of a chat.
    """
    @swagger_auto_schema(
        responses={200: MessageSerializer,
                   400: "Error message"}
                   )
    def post(self, request, *args, **kwargs):
        """
        # Handle POST request to get all messages of a chat.
        * Path params : chat_id.
        * Request body : NA.
        * Response : A HTTP response of success message or failure as JSON data.
        """
        user = request.user
        member = get_member(user)
        if not member:
            return HTTP_400(error={"member": ["Not a member, login and try again."]})
        
        organization = get_member_organization(member)
        if not organization:
            return HTTP_400(error={"organization": ["Not a member of any organization, login and try again."]})
        
        receiver_id = request.data.get("receiver_id")
        if not receiver_id:
            return HTTP_400(error={"receiver_id": ["Please provide receiver id"]})
        try:
            receiver = Member.objects.get(id=receiver_id)
        except Member.DoesNotExist:
            return HTTP_400(error={"receiver_id": ["Receiver does not exist"]})
        
        chat = Message.objects.filter(Q(sender=member,receiver=receiver)| Q(receiver=member,sender=receiver)).order_by('timestamp')
        serializer = ChatSerializer(chat, many=True)
        return HTTP_200(data=serializer.data)
        
