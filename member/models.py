from django.db import models
from accounts.models import User

# Create your models here.
import uuid

class Member(models.Model):
    """member model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    user = models.ForeignKey("accounts.User",on_delete=models.CASCADE,related_name="member")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    organization = models.ForeignKey("organization.Organization",on_delete=models.CASCADE,related_name="member")
    role = models.ForeignKey("organization.Role",on_delete=models.CASCADE,related_name="member")
    profile_image = models.ImageField(
        upload_to="media/members/profile_images/", blank=True, null=True
    )
    
    class Meta:
        """meta data"""
        verbose_name = "Member"
        verbose_name_plural = "Members"
        ordering = ["-created_at"]
        unique_together = ["user", "organization"]

    def __str__(self) -> str:
        return self.user.username