from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    achieved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specifications = models.TextField()

class ProductSustainability(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sustainability_info = models.TextField()

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='Pending')

