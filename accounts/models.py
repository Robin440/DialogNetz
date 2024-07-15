from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser,BaseUserManager

class User(AbstractUser):
    """User model for handle user data"""
    username = models.CharField(unique=True,max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20,blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_used_org =models.ForeignKey("organization.Organization",on_delete=models.CASCADE,related_name="user",blank=True,null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def __str__(self):
        return self.username
    class Meta:
        """meta class for additional functionality"""
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']
        # indexes = [
        #     models.Index(fields=['username']),
        #     models.Index(fields=['email']),
        #     ]
        

