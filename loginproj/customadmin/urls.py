from django.urls import include, path
from . import views
app_name='customadmin'
urlpatterns = [
    path('adminsignin',views.adminsignin,name = 'adminsignin'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('adminsignout',views.adminsignout,name = 'adminsignout'),
    path('manageusers',views.manageusers,name = 'manageusers'),
    path('deleteuser/<int:userid>',views.deleteuser,name = 'deleteuser'),
    path('edituser/<int:userid>',views.edituser,name = 'edituser'),
    path('createuser',views.createuser,name = 'createuser'),
]