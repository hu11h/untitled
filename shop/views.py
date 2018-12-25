from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.contrib.auth.decorators import login_required

@login_required
def search(request):
    q = request.GET.get('q')
    error_msg = ''
    category = None
    categories = Category.objects.all()

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'shop/result.html', {'error_msg': error_msg})

    product_list_search = Product.objects.filter(name__icontains=q)
    return render(request, 'shop/result.html', {'error_msg': error_msg,
                                               'category': category, 'categories': categories,'product_list_search': product_list_search})
@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(categories, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'category': category, 'categories': categories, 'products': products})

@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'shop/product/detail.html', {'product': product})

@login_required
def index(request):
    return render(request, 'shop/index.html')

@login_required
def xxx(request):
    return render(request, 'shop/xxx.html')
def m1(request):
    return render(request, 'shop/1.html')
def m2(request):
    return render(request, 'shop/2.html')
def m3(request):
    return render(request, 'shop/3.html')
def m4(request):
    return render(request, 'shop/4.html')
def m5(request):
    return render(request, 'shop/5.html')
def m6(request):
    return render(request, 'shop/6.html')
def m7(request):
    return render(request, 'shop/7.html')
def m8(request):
    return render(request, 'shop/8.html')
def m9(request):
    return render(request, 'shop/9.html')
def m10(request):
    return render(request, 'shop/10.html')
def market(request):
    return render(request,'shop/market.html')
def add1(request):
    return render(request,'shop/add1.html')

@login_required
def product2_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(categories, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list2.html',
                  {'category': category, 'categories': categories, 'products': products})

@login_required
def product2_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'shop/product/detail2.html', {'product': product})