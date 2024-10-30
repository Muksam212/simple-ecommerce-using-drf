from django.db import models

from root.utils import BaseModel
from users.models import User
# Create your models here.

class Customer(BaseModel):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "customers", null = True)

    def __str__(self):
        return f"{self.user.username}"


class Category(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique = True)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return f"{self.name}"
    
class ProductImage(BaseModel):
    name = models.CharField(max_length=100, unique = True, null = True, blank = False)
    image = models.ImageField(upload_to="product/images", null = True, blank = False)

    def __str__(self):
        return f"{self.name}"


class Product(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique = True, null = True)
    product_image = models.ForeignKey(ProductImage, on_delete = models.CASCADE, related_name="product_image", null = True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "users_order")
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "order_products")
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    

class Review(BaseModel):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = "product_review", null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user_review", null = True)
    rating = models.PositiveIntegerField(default = 1)
    comment = models.TextField(null = True, blank = False)

    def __str__(self):
        return f"Review by {self.user.username} on {self.product.name}"
    

class WishList(BaseModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user_wishlist", null = True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = "user_product", null = True)
    added_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username}"
    

class ShippingAddress(BaseModel):
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = "user_shipping_address")
    address = models.TextField(null = True, blank = False)
    city = models.CharField(max_length=100, unique = True, null = True, blank = False)
    state = models.CharField(max_length=100, unique = True, null = True, blank = False)
    postal_code = models.CharField(max_length=100, unique = True, null = True, blank = False)
    country = models.CharField(max_length=100, unique = True, null = True, blank = False)


    def __str__(self):
        return f"{self.order.user.username}"
    

class BillingAddress(BaseModel):
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = "user_billing_address")
    address = models.TextField(null = True, blank = False)
    city = models.CharField(max_length=100, unique = True, null = True, blank = False)
    state = models.CharField(max_length=100, unique = True, null = True, blank = False)
    postal_code = models.CharField(max_length=100, unique = True, null = True, blank = False)
    country = models.CharField(max_length=100, unique = True, null = True, blank = False)


    def __str__(self):
        return f"{self.order.user.username}"
    

class Payment(BaseModel):
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = "user_payment", null = True)
    payment_method = models.CharField(max_length=50, choices =[
        ("Khalti", "Khalti"),
        ("Cod", "Cod"),
        ("None", "None")
    ])
    status = models.CharField(max_length=100, choices = [
        ("Completed", "Completed"),
        ("Pending", "Pending"),
        ("Failed", "Failed"),
        ("None", "None")
    ])
    
    def __str__(self):
        return f"Payment for Order {self.order.id}"