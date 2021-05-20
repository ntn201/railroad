from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('seat/', views.SeatList.as_view()),
    path('seat/<int:pk>/', views.SeatDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)