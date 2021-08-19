from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email="test@gmail.com")
        user.set_password(validated_data['password'])
        user.save()
        return user