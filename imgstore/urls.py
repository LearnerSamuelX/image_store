from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #use the following to test form validation
    path('store',views.store,name='store'),

    #path for image upload redirecting
    path('imagebox', views.imagebox,name='imagebox')
]