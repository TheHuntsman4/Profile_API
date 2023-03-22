from rest_framework import serializers
from .models import Profile as ProfileModel


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfileModel
        fields=["id","name","profile_image"]