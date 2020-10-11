from django.urls import path
from . import views

urlpatterns = [
    path('login1',views.login1),
    path('bootstrap',views.bootstrap),
    path('logout1',views.logout1)
]