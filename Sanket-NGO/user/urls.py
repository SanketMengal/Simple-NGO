from django.urls import path,include
from . import views
urlpatterns=[
    path('index/',views.index),
    path('home/', views.index),
    path('', views.index),
    path('about/', views.about),
    path('gallery/', views.gallery),
    path('video/', views.video),
    path('blog/', views.blog),
    path('my/', views.my),
    path('membership/', views.membership),
    path('donate/', views.donate),
    path('contact/', views.contact),
    path('causes/', views.causes),
    path('details/', views.vdodetails),
    path('bdetails/', views.blogdetails),


]