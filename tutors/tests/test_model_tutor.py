from decimal import *
from django.test import TestCase
from ..models import Tutor



# TODO: can be expanded to check every field's format, but i guess not neccessary for this task.
class TutorModelTestCase(TestCase):

    def setUp(self):
        Tutor.objects.all().delete()
        self.tutor = Tutor(name='Bob',
                           description='super tutor',
                           subject='art',
                           score=2.2)
        self.tutor.save()

    def test_create_a_movie(self):
        self.assertEqual(1, Tutor.objects.count())

    def test_update_a_tutor(self):
        self.tutor.name = 'Someone'
        self.tutor.description = 'something is here'
        self.tutor.subject = 'geography'
        self.tutor.score = 2.4
        self.tutor.save()

        updated = Tutor.objects.get(name=self.tutor.name)

        self.assertEqual(self.tutor.name, updated.name)
        self.assertEqual(self.tutor.description, updated.description)
        self.assertEqual(self.tutor.subject, updated.subject)
        self.assertEqual(round(Decimal(self.tutor.score), 2), updated.score)

    def test_delete_a_tutor(self):
        self.tutor.delete()

        self.assertEqual(0, Tutor.objects.count())
