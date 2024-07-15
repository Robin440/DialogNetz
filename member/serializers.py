from rest_framework import serializers
from member.models import Member,Message
from organization.serializers import *
from accounts.serializers import UserSerializers


class MemberSerializer(serializers.ModelSerializer):
    """
    Member serializers

    """
    organization = OrganizationSerializers()
    role = RoleSerializer()
    user = UserSerializers()
    class Meta:
        """
        Meta class for MemberSerializer
        """
        model = Member
        fields = "__all__"


class MemberValidationSerializer(serializers.ModelSerializer):
    """
    Member validation serializers

    """

    class Meta:
        """
        Meta class for MemberValidationSerializer
        """
        model = Member
        fields = "__all__"



class MessageSerializer(serializers.ModelSerializer):
    """
    Message serializers
    """
    class Meta:
        """
        Meta class for MessageSerializer
        """
        model = Message
        fields = "__all__"


class MessageValidationSerialzer(serializers.ModelSerializer):
    """
    Message validation serializers
    """
    class Meta:
        """
        Meta class for MessageValidationSerialzer
        """
        model = Message
        fields = "__all__"


class ChatSerializer(serializers.ModelSerializer):
    """
    Chat serializers
    """

    sender = MemberSerializer(read_only=True)
    receiver = MemberSerializer(read_only=True)
    class Meta:
        """
        Meta class for ChatSerializer
        """
        model = Message
        fields = "__all__"

        