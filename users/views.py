from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from users.models import UserProfile
from users.serializers import UserProfileRetrieveSerializer


class UserProfileRetrieveView(RetrieveAPIView):
    serializer_class = UserProfileRetrieveSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        current_user = self.request.user
        if current_user.username == UserProfile.username:
            return current_user
