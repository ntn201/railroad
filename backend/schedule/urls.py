from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('schedule/', views.ScheduleList.as_view()),
    path('schedule/<int:pk>/', views.ScheduleDetail.as_view()),
    path('schedule/addschedule/', views.AddSchedule.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)