from rest_framework import serializers
from .models import usermanager

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = usermanager
		fields ='__all__'