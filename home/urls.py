
from django.urls import path
from . import views

urlpatterns=[
    path('',views.hello,name='hello'),
    path('helloworld',views.hellohtml,name='html')
]