from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #use the following to test form validation
    path('store',views.store,name='store'),

    #path for image upload redirecting
    path('imagebox', views.imagebox,name='imagebox'),

    #path for delete photo
    path('imagebox/image_deleted/<int:id_num>',views.image_delete,name='image_delete'),

    #path for content change (caption in this case)
    path('imagebox/caption_changed/<int:id_num>', views.caption_change, name='caption_change')
]