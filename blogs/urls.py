from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/', views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('create_post/',views.create_post,name='create_post'),
    path('my_posts/',views.my_posts,name='my_posts'),
    path('post/<str:id>',views.post,name='post'),
]
