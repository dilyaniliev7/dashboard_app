from django.db import models

class Country(models.Model):
    MAX_LEN_COUNTRY_NAME = 200
    
    name = models.CharField(max_length=MAX_LEN_COUNTRY_NAME)
    

class Gender(models.Model):
    MAX_LEN_GENDER_NAME = 200
    
    name = models.CharField(max_length=MAX_LEN_GENDER_NAME)
    
    
class CustomerType(models.Model):
    MAX_LEN_CUSTOMER_NAME = 200

    name = models.CharField(max_length=MAX_LEN_CUSTOMER_NAME)


class Branch(models.Model):
    MAX_LEN_BRANCH_NAME = 200
    MAX_LEN_DESCRIPTION = 200

    name = models.CharField(max_length=MAX_LEN_BRANCH_NAME)
    description = models.CharField(max_length=MAX_LEN_DESCRIPTION)


class ProductLine(models.Model):
    MAX_LEN_PRODUCT_NAME = 200

    name = models.CharField(max_length=MAX_LEN_PRODUCT_NAME)


class Payment(models.Model):
    MAX_LEN_PAYMENT_NAME = 200
    MAX_LEN_CATEGORY_NAME = 200

    name = models.CharField(max_length=MAX_LEN_PAYMENT_NAME)
    category = models.CharField(max_length=MAX_LEN_CATEGORY_NAME)


class SuperMarketSales(models.Model):
    MAX_DIGITS_NUM = 10
    DECIMAL_PLACES = 2

    unit_price = models.DecimalField(max_digits=MAX_DIGITS_NUM, decimal_places=DECIMAL_PLACES)
    quantity = models.IntegerField()
    date = models.DateField()

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    customer_type = models.ForeignKey(CustomerType, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
