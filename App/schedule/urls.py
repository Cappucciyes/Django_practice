from django.urls import path
from .views import CreateSchedule, DetailSchedule, EditSchedule, DeleteSchedule

urlpatterns = [
    path('create/', CreateSchedule.as_view(), name="schedule_create"),
    path('<uuid:pk>/',DetailSchedule.as_view(), name="schedule_detail"),
    path('<uuid:pk>/edit/', EditSchedule.as_view(), name="schedule_edit"),
    path('<uuid:pk>/delete/', DeleteSchedule.as_view(), name="schedule_delete"),
]
