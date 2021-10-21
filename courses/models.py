from django.db import models
from django.db.models.base import Model
import uuid


class Course(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    date_created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self) -> str:
        return self.title


class Membership(models.Model):
    MEMBERSHIP_CHOICES = [
        ('free', 'Free'),
        ('premium', 'Premium')
    ]
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, unique=True)
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, default='free', max_length=20)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)


    def __str__(self) -> str:
        return self.membership_type





