from django.db import models

# Create your models here.

import uuid


class Organization(models.Model):
    """model for organization"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        """meta data"""
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name
    

class Role(models.Model):
    """model for roles"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        """meta data"""
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        ordering = ["-updated_at"]
    def __str__(self):
        return self.name


class Department(models.Model):
    """department model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,related_name="department",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        """meta data"""
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ["-updated_at"]
    def __str__(self):
        return self.name