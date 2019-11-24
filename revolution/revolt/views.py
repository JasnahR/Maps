from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author' : 'JasnahR',
        'title' : 'blog post 1'
    },
    {
        'author' : 'JasnahQ',
        'title' : 'blog post 2'
    }
]
st = "demo"
year = []
for i in range(1700, 1850):
    year.append(str(i))


def home(request):
    context = {
        'posts': posts,
        'st': st,
        'year': year
    }
    return render(request, 'revolt/home.html', context)

# Create your views here.
