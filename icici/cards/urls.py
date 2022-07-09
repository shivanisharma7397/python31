
from django.contrib import admin
from django.urls import path,include
from cards import views
urlpatterns = [
    path('credit/', views.credit_views),
    path('fastag/', views.fast_tag_views),
    path('creditdata/', views.credit_data),
    path('fastagdata/', views.fast_tag_data),

]
