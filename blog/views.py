from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author":"Ruben",
        "title":"Blog Post 1",
        "content": "First post content",
        "date_posted": "18 de Febrero"
    },
    {
        "author":"Yoni",
        "title":"Blog Post 2",
        "content": "Second post content",
        "date_posted": "19 de Febrero"
    }
]


# Create your views here.
def home(request):
    context = {"posts":posts}
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html",{"title":"About"})