from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('route/', views.RouteList.as_view()),
    path('route/<int:pk>/', views.RouteDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)