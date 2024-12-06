from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=20)
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    weight = models.FloatField()
    description = models.TextField()
    size = models.IntegerField()
    color = models.CharField(max_length=20)
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.product_name

class Inventory(models.Model):
    quantity_in_stock = models.IntegerField()
    last_restocked = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Supplier(models.Model):
    supplier_company_name = models.CharField(max_length=20)
    contact_name = models.TextField()
    email = models.EmailField(max_length=255)
    address = models.TextField()
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)

class Discount(models.Model):
    discount_code = models.CharField(max_length=20)
    discount_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    date_joined = models.DateField()

class Review(models.Model):
    rating = models.IntegerField()
    review_text = models.TextField(null=True)
    review_date = models.DateField()
    is_approved = models.BooleanField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Ordering(models.Model):
    order_date = models.DateField()
    total_amount = models.IntegerField()
    order_status = models.CharField(max_length=20)
    shipping_address = models.TextField()
    payment_method = models.CharField(max_length=20)
    tracking_number = models.CharField(max_length=20)
