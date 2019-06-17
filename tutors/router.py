from rest_framework.routers import DefaultRouter
from .views import TutorViewSet


router = DefaultRouter()


router.register('tutors', TutorViewSet, base_name='tutor')


