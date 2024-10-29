from django.urls import path
from .import views

urlpatterns = [
  path('', views.home, name='home'),
  path('login/', views.login_view, name='login'),
  path('signup/', views.showform, name='signup'),
  path('user_profile/', views.user_profile, name='userprofile'),
  path('base/', views.base),
  path('home/', views.home, name='home'),
  path('logout/', views.logout, name='logout'),
  path('blog/', views.blog, name='blog'),
  path('viewblogs/', views.all_blog, name='viewblog'),
  path('changepassword/', views.changepassword, name='changepassword'),
  path('update/<int:id>/', views.update_user, name='update_user'),
  path('delete/<int:id>/', views.delete_user, name='delete_user'),
  path('deleteblog/<int:id>/', views.delete_blog, name='delete_blog'),
  path('delete_login_user/<int:id>', views.delete_login_user, name='delete'),
  path('update_blog/<int:id>/', views.update_blog, name="update_blog"),
  path('about/', views.about_section, name='about')
   
]
