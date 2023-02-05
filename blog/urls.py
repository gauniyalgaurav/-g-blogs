from django.urls import path
from . import views

urlpatterns = [
    path('  ',views.home,name='home'),
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('sign',views.sign,name='sign'),
    path('about',views.about,name='about'),
    path('write',views.write,name='write'),
    path('logout',views.logout,name='logout'),
    path('posts',views.posts,name='posts'),
]