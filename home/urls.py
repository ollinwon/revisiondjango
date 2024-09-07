
from django.urls import path
from . import views

urlpatterns=[
    path('',views.delete,name='hello'),
    path('helloworld',views.hellohtml,name='html'),
    path('insertuser',views.insertuser,name='insert'),
    path('displayuser',views.displayuser,name='display'),
    path('filtereddata',views.filtereddata,name='filter'),
    path('updatesingle',views.updatesingle,name='update'),
    path('ordereddata',views.ordereddata,name='order'),
    path('insertpostdata',views.insertpostdata,name='post'),
    path('deletecriteria',views.deletecriteria,name='delete'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('hashregister',views.hashregister,name='hashregister'),
    path('upload_image',views.upload_image,name='upload_image'),

]
