from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('ticket/', views.TicketList.as_view()),
    path('ticket/<int:pk>/', views.TicketDetail.as_view()),
    path('ticket/create/', views.TicketCreator.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)