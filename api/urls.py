from django.urls import path, include
from accounts.views import *
from organization.views import *
from member.views.member_views import *
from member.views.message_views import *
from accounts.views.account_views import *


urlpatterns = [
    path("login/", LoginAPI.as_view()),
    path('logout/',LogoutAPI.as_view()),
    path('register/',RegisterAPI.as_view()),
    path("member-list-create/", MemberCreateListAPI.as_view()),
    path("verify-member-otp/", OTPVerifyMemberAPI.as_view()),
    # path("csrf-token/", csrf_token),
    path("send-message/",SendMessageAPIView.as_view()),
    path("receive-message/<uuid:receiver_id>/",ReceiveMessageAPI.as_view()),
    path("send-message/<uuid:sender_id>/",SendMessageAPIView.as_view()),
    path('current-user/', CurrentUserAPI.as_view(), name='current-user'),
    path("chat-view/",ChatviewAPI.as_view()),
]
    