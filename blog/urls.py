from django.urls import path
from .views import loginUser,register,home,logoutUser,add_blog,blog_view,my_blog

urlpatterns = [
    path('register', register,name='register'),
    path('login', loginUser,name='login'),
    path('logout/', logoutUser,name='logout'),
    path('add_blog',add_blog,name = 'add_blog'),
    path('',home,name='home'),
    path('my_blog',my_blog,name='my_blog'),
    path('view/<int:id>',blog_view,name='blog_view'),
]

