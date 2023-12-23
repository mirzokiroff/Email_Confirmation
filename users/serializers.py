from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from users.models import UserProfile


class UserProfileRetrieveSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['is_superuser', 'is_staff', 'groups', 'user_permissions', 'is_active', 'date_joined']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class RegisterSerializer(ModelSerializer):
    password = CharField(write_only=True)
    confirm_password = CharField(write_only=True)

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")

        return data

    class Meta:
        fields = ['username', 'email', 'password', 'confirm_password']
