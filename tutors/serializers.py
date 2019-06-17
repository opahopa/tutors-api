from rest_framework import serializers
from .models import Tutor


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ('id', 'name', 'subject', 'description', 'score', 'register_date')
        read_only_fields = ('id', 'register_date', 'score',)
