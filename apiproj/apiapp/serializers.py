from rest_framework import serializers
from django.contrib.auth.models import User
from apiapp.models import clients, projects
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = clients
        fields = '__all__'
    

class ProjectsSerializer(serializers.ModelSerializer):
    # uname = UserSerializer(many=True, read_only=True)
    class Meta:
        model = projects
        fields = '__all__'
