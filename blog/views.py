from django.shortcuts import render
from . models import Post,Category
# Create your views here.
def home(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
   
    data = {
        'posts':posts,
        'cats':cats
        
    }
    return render(request, 'home.html',data)

def post1(request,url):
    posts = Post.objects.filter(url=url)

    return render(request,'post.html',{"posts":posts})


def category(request, url):
    cat = Category.objects.get(url = url)
    posts = Post.objects.filter(cat=cat)
    return render(request, 'category.html',{'cat':cat, 'posts':posts})
