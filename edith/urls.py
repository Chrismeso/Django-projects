
from django.contrib import admin
from django.urls import path
from edith import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('gallery/', views.gallery),
]
