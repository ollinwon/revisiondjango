from rest_framework import serializers
from home.models import RegisterForm

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegisterForm
        fields='__all__'