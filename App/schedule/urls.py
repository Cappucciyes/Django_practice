from django.urls import path
from .views import CreateSchedule, DetailSchedule

urlpatterns = [
    path('create/', CreateSchedule.as_view(), name="schedule_create"),
    path('<uuid:pk>/',DetailSchedule.as_view(), name="schedule_detail")
]
