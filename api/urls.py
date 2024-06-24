from django.urls import path,include
from accounts.views import *
from organization.views import *
from member.views import *




urlpatterns = [
    path('login/',LoginAPI.as_view()),
    path('member-list-create/',MemberCreateListAPI.as_view())
   

]
