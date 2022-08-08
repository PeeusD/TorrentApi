from pyexpat import model
from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        feilds = '__all__'