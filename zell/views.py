from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from .models import Category, Furniture, AdditionalImages

def main(request):
    categories = Category.objects.all()
    context = {'categories': categories} 
    return render(request, 'zell/main.html', context)

def products(request):
    categories = Category.objects.all()
    context = {'categories': categories} 
    return render(request, 'zell/products.html', context)

def main_detail(request, pk):
    main = Category.objects.get(id=pk)
    main_details = Furniture.objects.filter(category=pk)
    context = {'main':main, 'main_details':main_details}
    return render(request, 'zell/main_detail.html', context)

def product_detail(request, category_id, product_id):
    category_object = Category.objects.get(id=category_id) 
    product_object = Furniture.objects.get(id=product_id)
    additional_images = AdditionalImages.objects.filter(furniture=product_id)
    context = {
        'category_object':category_object,
        'category_id':category_id,
        'product_object':product_object,
        'additional_images':additional_images,
    }
    return render(request, 'zell/product_detail.html', context)

def about_us(request):
    return render(request, 'zell/about_us.html')

def contacts(request):
    return render(request, 'zell/contacts.html')

def other_page(request, page):
    try:
        template = get_template(page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))