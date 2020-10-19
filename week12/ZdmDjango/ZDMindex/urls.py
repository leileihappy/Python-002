from . import views
from django.urls import path

urlpatterns = [
    path('phones',views.phones),
]