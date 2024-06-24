from rest_framework import serializers
from organization.models import *

class OrganizationSerializers(serializers.ModelSerializer):
    """
    Organization serializer

    """

    class Meta:
        model = Organization
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    """
    Role serializer

    """
    class Meta:
        model = Role
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    """
    Department serializer

    """

    class Meta:
        model = Department
        fields = "__all__"