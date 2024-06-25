from accounts.models import User
from organization.models import Organization
from utils.responses import *
from member.models import Member

import random
import string



def get_user_organization(user):
    """
    Get the organization of a user
    """
    try:
        organization_instance = Organization.objects.get(id = user.last_user_org.id)
    except Organization.DoesNotExist:
        return HTTP_400(error={"organization":["Organization is not found."]})
    
    return organization_instance


def get_member_organization(member):
    """
    Get the organization of a member
    
    """
    try:
        organization_instance = Organization.objects.get(id = member.organization.id)
    except Organization.DoesNotExist:
        return HTTP_400(error={"organization":["Organization is not found."]})
    return organization_instance


def get_member(user):
    """
    Get the member instance of a user
    """
    try:
        member_instance = Member.objects.get(user=user.id)
    except Member.DoesNotExist:
        return HTTP_400(error={"member":["Member is not found."]})
    return member_instance


def is_admin(member):
    """
    Check if a member is an admin

    """

    if member.role.name == "Admin":
        return True
    return False



def generate_unique_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))