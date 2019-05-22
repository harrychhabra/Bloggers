from django.db import models

# Create your models here.


class Blog(models.Model):
	title = models.CharField(max_length = 255, blank = False)
	content = models.TextField(blank = False)
	date = models.DateTimeField(auto_now_add = True, blank = False)


class Trending(models.Model):
	title = models.CharField(max_length = 255, blank = False)
	content = models.TextField(blank = False)