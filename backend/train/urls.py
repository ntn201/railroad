from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('train/', views.TrainList.as_view()),
    path('train/<int:pk>', views.TrainDetail.as_view()),
    path('train/createtrain/', views.TrainCreator.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)