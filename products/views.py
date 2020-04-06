from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Product
from accounts.models import Favourite
from .forms import ReviewForm
import operator
from django.db.models import Q
from functools import reduce
from django.db.models import Avg


ITEMS_PER_PAGE = 3


def all_products(request):
    filter_keys = [*request.GET]
    if 'page' in filter_keys:
        filter_keys.remove('page')

    if len(filter_keys) > 0:
        products = Product.objects.filter(
            reduce(operator.or_, (Q(tag__value=x)for x in filter_keys)))

    else:
        products = Product.objects.all()

    paginator = Paginator(products, ITEMS_PER_PAGE)

    page = request.GET.get('page')

    # If there is no page parameter in URL, set page to 1

    if(page is None):
        page = 1

    products = paginator.page(page)

    return render(request, "products.html", {"products": products})


def face_products(request):
    products = Product.objects.all().filter(category='F')

    filter_keys = [*request.GET]
    if 'page' in filter_keys:
        filter_keys.remove('page')

    if len(filter_keys) > 0:
        products = products.filter(
            reduce(operator.or_, (Q(tag__value=x)for x in filter_keys)))

    paginator = Paginator(products, ITEMS_PER_PAGE)

    page = request.GET.get('page')

    # If there is no page parameter in URL, set page to 1

    if(page is None):
        page = 1

    products = paginator.page(page)
    return render(request, "products.html", {"products": products})


def body_products(request):
    products = Product.objects.all().filter(category='B')

    filter_keys = [*request.GET]
    if 'page' in filter_keys:
        filter_keys.remove('page')

    if len(filter_keys) > 0:
        products = products.filter(
            reduce(operator.or_, (Q(tag__value=x)for x in filter_keys)))

    paginator = Paginator(products, ITEMS_PER_PAGE)

    page = request.GET.get('page')

    # If there is no page parameter in URL, set page to 1

    if(page is None):
        page = 1

    products = paginator.page(page)
    return render(request, "products.html", {"products": products})


def product_detail(request, pk):
    """
    Create a view that returns a single
    Product object based on the product ID (pk) and
    render it to the 'productdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')

        else:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.owner = request.user
                review.product = product
                review.save()

            return redirect(product_detail, product.pk)

    else:
        form = ReviewForm()
        review_count = product.reviews.filter(approved=True).count()
        sum = 0 
        avg = 0 
        if review_count > 0:
            for score in product.reviews.filter(approved=True).values("score"):
                sum += score["score"]
            avg = sum / review_count 

        is_favourite = False
        if request.user.is_authenticated:
            user = request.user 
            if Favourite.objects.filter(user=user, product=product).count() > 0:
                is_favourite = True
        return render(request, "productdetail.html", {'product': product,
                                                      'form': form,
                                                      'is_favourite': is_favourite,
                                                      'score': avg,
                                                      'review_count': review_count})


# View for Product Types

def cleanser_products(request):
    products = Product.objects.all().filter(product_type='C')
    paginator = Paginator(products, ITEMS_PER_PAGE)

    page = request.GET.get('page')

    # If there is no page parameter in URL, set page to 1

    if(page is None):
        page = 1

    products = paginator.page(page)
    return render(request, "products.html", {"products": products})


def exfoliator_products(request):
    products = Product.objects.all().filter(product_type='EX')
    paginator = Paginator(products, ITEMS_PER_PAGE)

    page = request.GET.get('page')

    # If there is no page parameter in URL, set page to 1

    if(page is None):
        page = 1

    products = paginator.page(page)
    return render(request, "products.html", {"products": products})


def serum_products(request):
    products = Product.objects.all().filter(product_type='SE')
    paginator = Paginator(products, ITEMS_PER_PAGE)

    page = request.GET.get('page')

    # If there is no page parameter in URL, set page to 1

    if(page is None):
        page = 1

    products = paginator.page(page)
    return render(request, "products.html", {"products": products})


def moisturiser_products(request):
    products = Product.objects.all().filter(product_type='M')
    paginator = Paginator(products, ITEMS_PER_PAGE)

    page = request.GET.get('page')

    # If there is no page parameter in URL, set page to 1

    if(page is None):
        page = 1

    products = paginator.page(page)
    return render(request, "products.html", {"products": products})


def sunscreen_products(request):
    products = Product.objects.all().filter(product_type='SU')
    paginator = Paginator(products, ITEMS_PER_PAGE)

    page = request.GET.get('page')

    # If there is no page parameter in URL, set page to 1

    if(page is None):
        page = 1

    products = paginator.page(page)
    return render(request, "products.html", {"products": products})


def toner_products(request):
    products = Product.objects.all().filter(product_type='T')
    paginator = Paginator(products, ITEMS_PER_PAGE)

    page = request.GET.get('page')

    # If there is no page parameter in URL, set page to 1

    if(page is None):
        page = 1

    products = paginator.page(page)
    return render(request, "products.html", {"products": products})


def masks_products(request):
    products = Product.objects.all().filter(product_type='FM')
    paginator = Paginator(products, ITEMS_PER_PAGE)

    page = request.GET.get('page')

    # If there is no page parameter in URL, set page to 1

    if(page is None):
        page = 1

    products = paginator.page(page)
    return render(request, "products.html", {"products": products})


def eye_products(request):
    products = Product.objects.all().filter(product_type='E')
    paginator = Paginator(products, ITEMS_PER_PAGE)

    page = request.GET.get('page')

    # If there is no page parameter in URL, set page to 1

    if(page is None):
        page = 1

    products = paginator.page(page)
    return render(request, "products.html", {"products": products})


def chemical_products(request):
    products = Product.objects.all().filter(product_type='CH')
    paginator = Paginator(products, ITEMS_PER_PAGE)

    page = request.GET.get('page')

    # If there is no page parameter in URL, set page to 1

    if(page is None):
        page = 1

    products = paginator.page(page)
    return render(request, "products.html", {"products": products})
