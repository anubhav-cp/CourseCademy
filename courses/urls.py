from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name='home'),
    path('view-course/<str:pk>/', views.viewCourse, name='view-course')
]