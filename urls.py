from django.urls import path
from . import views

urlpatterns = [
    path('add-product/', views.add_product, name='add_product'),
    path('add-product-success/', views.add_product_success, name='add_product_success'),
    path('upload-product-images/', views.upload_product_images, name='upload_product_images'),
    path('upload-product-images-success/', views.upload_product_images_success, name='upload_product_images_success'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('edit-product-success/', views.edit_product_success, name='edit_product_success'),
    path('manage-product-sustainability/', views.manage_product_sustainability, name='manage_product_sustainability'),
    path('manage-product-sustainability-success/', views.manage_product_sustainability_success, name='manage_product_sustainability_success'),
    path('categorize-products/', views.categorize_products, name='categorize_products'),
    path('categorize-products-success/', views.categorize_products_success, name='categorize_products_success'),
    path('generate-inventory-report/', views.generate_inventory_report, name='generate_inventory_report'),
    path('generate-inventory-report-success/', views.generate_inventory_report_success, name='generate_inventory_report_success'),
    path('achieve-product/', views.achieve_product, name='achieve_product'),
    path('achieve-product-success/', views.achieve_product_success, name='achieve_product_success'),
    path('manage-inventory/', views.manage_inventory, name='manage_inventory'),
    path('manage-inventory-success/', views.manage_inventory_success, name='manage_inventory_success'),
    path('cancel-item/', views.cancel_item, name='cancel_item'),
    path('cancel-item-success/', views.cancel_item_success, name='cancel_item_success'),
]
