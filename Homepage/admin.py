from django.contrib import admin

from .models import Blog, Trending
# Register your models here.

admin.site.register(Blog)
admin.site.register(Trending)
