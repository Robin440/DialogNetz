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
    otp = models.IntegerField(null=True,blank=True)
    invitation_code = models.CharField(max_length=7,null=True,blank=True)
    profile_image = models.ImageField(
        upload_to="media/members/profile_images/", blank=True, null=True
    )
    is_invited = models.BooleanField(default=True)
    connections = models.ManyToManyField("self", symmetrical=False, blank=True)
    
    class Meta:
        """meta data"""
        verbose_name = "Member"
        verbose_name_plural = "Members"
        ordering = ["-created_at"]
        unique_together = ["user", "organization"]

    def __str__(self) -> str:
        return self.user.username
    




from django.db import models
from django.utils import timezone
import uuid

class Message(models.Model):
    """Message model to store chat messages between members"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(Member, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Member, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    media = models.FileField(upload_to='media/messages/', blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.sender.name} to {self.receiver.name}: {self.content[:50]}"
