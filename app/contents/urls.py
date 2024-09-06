from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from contents.views import *

urlpatterns = [
    path('v1/token/', obtain_auth_token, name='get-token'),
    path('v1/request-add/', CreateRequestAPIView.as_view(), name='request-add'),
    path('v1/request/', ListRequestAPIView.as_view(), name='list-request'),
    path('v1/request/<int:pk>/', RetrieveRequestAPIView.as_view(), name='retrieve-request'),
    path('v1/message-add/', CreateRequestMessageAPIView.as_view(), name='message-add'),
    path('v1/messages/<int:pk>/', ListRequestMessageAPIView.as_view(), name='list-messages'),
]
