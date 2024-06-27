from django.urls import path,include
from accounts.views import *
from organization.views import *
from member.views.member_views import *




urlpatterns = [
    path('login/',LoginAPI.as_view()),
    path('member-list-create/',MemberCreateListAPI.as_view()),
    path('verify-member-otp/',OTPVerifyMemberAPI.as_view()),
     path('csrf-token/',csrf_token),    
   

]
