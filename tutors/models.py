from django.db import models


class Tutor(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    subject = models.CharField(max_length=255)
    register_date = models.DateField(auto_now_add=True)
    score = models.DecimalField(
        default=1.0,
        max_digits=2, decimal_places=1
    )



