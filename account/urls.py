from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_title='Welcome to the Developer zone'
admin.site.index_title='Welcome to the portal'
admin.site.site_header='Account dashboard'

urlpatterns=[
    path('',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]