from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^home/',views.index,name='index'),url(r'^login/',views.login,name='login')
    ,url(r'^find/',views.find,name='find'),url(r'^logout/',views.logout,name='logout'),
    url(r'^submit/',views.submit,name='submit'),url(r'^remove/',views.remove,name='remove'),url(r'^removeitem/',views.removeitem,name='removeitem')
    ,url(r'^show/',views.show,name='show'),url(r'^add/',views.add,name='add'),url(r'^display/',views.display,name='display')
    ]