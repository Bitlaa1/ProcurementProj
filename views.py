from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductImage, ProductSpecification, ProductSustainability, Order
from .forms import ProductForm, ProductImageForm, ProductSpecificationForm, ProductSustainabilityForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_product_success')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def add_product_success(request):
    return render(request, 'add_product_success.html')

def upload_product_images(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        product = Product.objects.get(id=product_id)
        
        images = request.FILES.getlist('images')
        for image in images:
            ProductImage.objects.create(product=product, image=image)
        
        specifications = request.POST.get('specifications')
        ProductSpecification.objects.create(product=product, specifications=specifications)
        
        return redirect('upload_product_images_success')
    else:
        products = Product.objects.all()
    return render(request, 'upload_product_images.html', {'products': products})

def upload_product_images_success(request):
    return render(request, 'upload_product_images_success.html')

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('edit_product_success')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

def edit_product_success(request):
    return render(request, 'edit_product_success.html')

def manage_product_sustainability(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        product = Product.objects.get(id=product_id)
        
        sustainability_info = request.POST.get('sustainability')
        ProductSustainability.objects.update_or_create(product=product, defaults={'sustainability_info': sustainability_info})
        
        return redirect('manage_product_sustainability_success')
    else:
        products = Product.objects.all()
    return render(request, 'manage_product_sustainability.html', {'products': products})

def manage_product_sustainability_success(request):
    return render(request, 'manage_product_sustainability_success.html')

def categorize_products(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        category = request.POST.get('category')
        
        product = Product.objects.get(id=product_id)
        product.category = category
        product.save()
        
        return redirect('categorize_products_success')
    else:
        products = Product.objects.all()
    return render(request, 'categorize_products.html', {'products': products})

def categorize_products_success(request):
    return render(request, 'categorize_products_success.html')

def generate_inventory_report(request):
    if request.method == 'POST':
        report_type = request.POST.get('report_type')
        # Generate the report (Implementation not shown here)
        return redirect('generate_inventory_report_success')
    return render(request, 'generate_inventory_report.html')

def generate_inventory_report_success(request):
    return render(request, 'generate_inventory_report_success.html')

def achieve_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        product = Product.objects.get(id=product_id)
        product.achieved = True
        product.save()
        return redirect('achieve_product_success')
    else:
        products = Product.objects.all()
    return render(request, 'achieve_product.html', {'products': products})

def achieve_product_success(request):
    return render(request, 'achieve_product_success.html')

def manage_inventory(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        stock_level = request.POST.get('stock_level')
        
        product = Product.objects.get(id=product_id)
        product.availability = stock_level
        product.save()
        
        return redirect('manage_inventory_success')
    else:
        products = Product.objects.all()
    return render(request, 'manage_inventory.html', {'products': products})

def manage_inventory_success(request):
    return render(request, 'manage_inventory_success.html')

def cancel_item(request):
    if request.method == 'POST':
        order_id = request.POST.get('order')
        order = Order.objects.get(id=order_id)
        order.status = 'Cancelled'
        order.save()
        return redirect('cancel_item_success')
    else:
        orders = Order.objects.all()
    return render(request, 'cancel_item.html', {'orders': orders})

def cancel_item_success(request):
    return render(request, 'cancel_item_success.html')
