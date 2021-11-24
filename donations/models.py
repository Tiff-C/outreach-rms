from django.db import models


class Product(models.Model):
    """ A class to define the product model """
    name = models.CharField("Product Name", max_length=50, blank=False)
    prod_id = models.CharField("Product ID", max_length=180, blank=False)
    price = models.DecimalField(
        "Product Price", max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    """ A class to define the order model """
    name = models.CharField("Full Name", max_length=70, blank=False)
    email = models.EmailField("Email Address", max_length=320, blank=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f'{self.id}-{self.date}-{self.name}'


class OrderLineItem(models.Model):
    """ A class to define the order line item model """
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.quantity} {self.product} @ {self.product.price}'
