from django.shortcuts import render
from blog.models import Post,Categoria

# Create your views here.

def blog (request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)

def categorie (request,categoria_id):
    categorie = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias = categorie)
    context = {'categorie':categorie,'posts':posts}
    return render(request, 'blog/categories.html',context)

def post (request,post_id):
    post = Post.objects.get(id=post_id)
    context = {'post':post}
    return render(request,'blog/post.html',context)