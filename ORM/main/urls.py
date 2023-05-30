from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('add/', views.add_page, name="add_page"),
    path('read/<blog_id>', views.read_blog, name="read_blog"),
    path('update/<blog_id>', views.update_blog, name="update_blog"),

]