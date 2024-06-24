from rest_framework import serializers
from member.models import Member
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