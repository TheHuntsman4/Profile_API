from django.urls import path, include
from .views import ProfileAPIView

urlpatterns = [
    path('api/',ProfileAPIView.as_view()),

]
