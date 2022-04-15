
from django.urls import path

from MochikaApp import views, admin
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('recetas/', views.recetas, name="recetas"),
    path('lista/', views.tienda, name="lista"),
    path('blog/', views.blog, name="blog"),
    path('restaurantes/', views.restaurantes, name="restaurantes"),
    path('contacto/', views.contacto, name="contacto"),
]
