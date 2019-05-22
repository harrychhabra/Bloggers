from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Homepage, name = 'homepage'),
    path('add-blog/', views.AddBlog, name = 'add_new_blog'),
]
