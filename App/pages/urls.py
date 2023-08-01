from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('schedule', HomePageView.as_view(), name='home'), # RUD of schedules
]