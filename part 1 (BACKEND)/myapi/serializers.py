from rest_framework import serializers
from . import models
from .models import Branches


class BranchesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Branches
        fields = '__all__'
