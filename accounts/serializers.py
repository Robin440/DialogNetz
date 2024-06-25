from rest_framework import serializers
from accounts.models import User
from organization.serializers import *


class UserSerializers(serializers.ModelSerializer):
    """
    User serializer

    """
    last_used_org = OrganizationSerializers(read_only=True)
    class Meta:
        """
        meta data
        """
        model = User
        exclude = ['password']


class UserValidationSerializers(serializers.ModelSerializer):
    """
    User serializer

    """
    class Meta:
        """
        meta data
        """
        model = User
        exclude = ['password']

