from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('$/',views.addstud1,name='addstud1')
]
