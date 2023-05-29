from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date
from .models import Blog
# Create your views here.

def home_page(request: HttpRequest):
    
    blogs = Blog.objects.all()

    return render(request, "main/home_page.html", {"blogs": blogs})

def add_page(request: HttpRequest):
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"],
                        contant=request.POST["contant"], 
                        is_published=request.POST["is_published"], 
                        publish_date=date.today())
        new_blog.save()
        return redirect("main:home_page")
    return render(request, "main/add_page.html")


