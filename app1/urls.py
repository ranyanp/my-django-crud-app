from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('save/', views.save, name='save'),
    path('update/<int:pk>', views.update, name='update'),
    path('data/', views.datas, name='data'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('edit/<int:id>/',views.edit, name='edit'),
    path('upload_photo/<int:id>/',views.upload_photo, name='upload_photo'),
     path('profile_save/',views.profile_save, name='profile_save'),

]