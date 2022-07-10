
from django.contrib import admin
from django.urls import path,include
from accounts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('carloan/', include('carloan.urls')),
    path('', include('home.urls')),
    path('account/', include('accounts.urls')),
    path('card/', include('cards.urls')),
    path('loan/', include('loans.urls')),
    path('insurance/', include('insurance.urls')),
    path('logout/', views.logout),
    path('accounts/', include('django.contrib.auth.urls')),

]
