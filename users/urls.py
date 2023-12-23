from django.urls import path, include
from .views import UserProfileRetrieveView

urlpatterns = [
    path('profile/', UserProfileRetrieveView.as_view(), name='profile')
]