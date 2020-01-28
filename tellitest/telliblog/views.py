from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

#  a view that define the home page

def home(requset):
    context = {
        'blogposts' : BlogPost.objects.all()
    }

    return render(requset, 'telliblog/home.html', context)


#  view that define about page
def about(requset):
    return render(requset, 'telliblog/about.html', {'title' : 'About'})
