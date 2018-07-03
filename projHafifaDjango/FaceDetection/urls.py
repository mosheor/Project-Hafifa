from django.urls import path
from . import views

app_name = 'FaceDetection'
urlpatterns = [
    path('', views.face_detection, name='face_detection'),
]
