
from django.contrib import admin
from django.urls import path
from carloan import views
urlpatterns = [
    path('empinfo/', views.empviews),
    path('empdata/', views.empdatafetch),
    path('clientinfo/', views.clientviews),
    path('clientdata/', views.clientdatafetch),
]
