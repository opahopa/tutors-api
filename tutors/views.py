from rest_framework import viewsets

from tutors.models import Tutor
from .serializers import TutorSerializer


class TutorViewSet(viewsets.ModelViewSet):
    ordering_fields = ['subject', 'register_date', 'score']

    queryset = Tutor.objects.all().order_by('-register_date')
    serializer_class = TutorSerializer