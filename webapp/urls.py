from django.urls import path
from webapp import views


urlpatterns=[
path('', views.home, name="base"),
path('register', views.register, name='register'),
path('my-login', views.my_login, name='my-login'),
path('dashboard', views.dashboard, name='dashboard'),
path('user-logout', views.user_logout, name='user-logout'),
path('create-record', views.create_record, name='create-record'),
path('update_record/<int:pk>', views.update_record, name='update_record'),
path('record/<int:pk>', views.singular_record, name='singular_record'),
path('delete_record/<int:pk>', views.delete_record, name='delete_record'),



]