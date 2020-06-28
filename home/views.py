from django.shortcuts import render, HttpResponse
from home.models import Blog

# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    blog = Blog.objects.all()
    context = {
        'blogs' : blog
    }
    return render(request, 'blog.html', context)

def blogs(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {
        'blogs' : blog
    }
    return render(request, 'blogpost.html', context)
