from django.urls import path
from . import views


urlpatterns = [
    path('', views.calculation),
    path('calc/add/', views.add),
    path('calc/sub/', views.sub),
    path('calc/mult/', views.mult),
    path('calc/div/', views.div),
]
