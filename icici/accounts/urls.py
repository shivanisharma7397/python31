
from django.contrib import admin
from django.urls import path,include
from accounts import views
urlpatterns = [
    path('saving/', views.saving_views),
    path('current/', views.current_views),
    path('fd/', views.fixed_deposit_views),
    path('fddata/', views.fixed_deposit_data),
    path('currentdata/', views.current_data),
    path('savingdata/', views.saving_data),

]
