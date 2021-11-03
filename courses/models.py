from django.db import models
from django.db.models.base import Model
import uuid
from membership.models import Membership



class Course(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    date_created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    type = models.ForeignKey(Membership, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.title + '  --->  ' + str(self.type)


class Chapter(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    video_url = models.URLField(max_length=300)
    date_created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    Course_name = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.title







