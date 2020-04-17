from django.shortcuts import render
from products.models import Product
from blog.models import Post


def do_search(request):
    """
    Search for products based on name
    """
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})


def do_blog_search(request):
    """
    Search for blog posts based on name
    """
    posts = Post.objects.filter(title__icontains=request.GET['q'])
    return render(request, "blogposts.html", {"posts": posts})
