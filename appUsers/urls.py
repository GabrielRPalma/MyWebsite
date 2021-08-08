from django.urls import path
from. import views
app_name='appUsers'
urlpatterns = [

    path('', views.index, name = 'index'),    
    path('discover/', views.discover, name ='discover'),
    path('welcome/', views.dashboard, name = 'dashboard'),
    path('register/', views.register, name ='register'),
    path('user_login/', views.user_login, name ='user_login'),
    path('user_logout/', views.user_logout, name ='user_logout'),

]
