from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Homepage, name = 'homepage'),
    path('add-blog/', views.AddBlog, name = 'add_new_blog'),
    path('view/blog/<str:id>', views.ViewBlog, name = 'view_blog'),
    path('view/trending/<str:id>', views.ViewTrending, name = 'view_trending'),
]
