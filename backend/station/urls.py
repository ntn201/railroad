from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('station/', views.StationList.as_view()),
    path('station/<int:pk>/', views.StationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)