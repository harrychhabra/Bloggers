from django.shortcuts import render, reverse, redirect

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django.template import loader
from .models import Blog, Trending

def Homepage(request):

	# Fetch all blogs
	blog_object = Blog.objects.all().order_by("-id")
	trending_object = Trending.objects.all()
	html_page = loader.get_template('Homepage.html')

	data = {
		'blog' : blog_object,
		'trending' : trending_object,
	}
	return HttpResponse(html_page.render({'data':data}))


@csrf_exempt
def AddBlog(request):

	if request.method == 'GET':
		html_page = loader.get_template('AddNewBlog.html')

		return HttpResponse(html_page.render({}), request)

	# POST request
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')

		blog_object = Blog()
		blog_object.title = title
		blog_object.content = content
		blog_object.save()

	return redirect(reverse('homepage'))

def ViewBlog(request, id):

	blog_object = Blog.objects.filter(pk__exact = id)

	if len(blog_object) > 0:
		data = {
			'object':blog_object[0],
		}
	else:
		data = {}

	html_page = loader.get_template('DetailedView.html')

	return HttpResponse(html_page.render({'data':data}))



def ViewTrending(request, id):

	trending_object = Trending.objects.filter(pk__exact = id)

	if len(trending_object) > 0:
		data = {
			'object':trending_object[0],
		}
	else:
		data = {}

	html_page = loader.get_template('DetailedView.html')

	return HttpResponse(html_page.render({'data':data}))