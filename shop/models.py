from django.db import models
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class ProductStatusType(models.IntegerChoices):
    published= 1, ("نمایش")
    draft= 2, ("عدم نمایش")


class ProductCategoryModel(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField(allow_unicode=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)


class ProductModel(models.Model):
    user = models.ForeignKey('accounts.User',on_delete=models.CASCADE)
    category=models.ManyToManyField(ProductCategoryModel)
    title=models.CharField(max_length=255)
    slug=models.SlugField(allow_unicode=True)
    image=models.ImageField(default="/default/product-image.png",upload_to="product/img/")
    breif_description=models.TextField(null=True,blank=True)
    description = models.TextField()
    stock=models.PositiveBigIntegerField(default=0)
    price=models.DecimalField(default=0,max_digits=10,decimal_places=0)
    discount_price=models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(100)])
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    status=models.IntegerField(choices=ProductStatusType.choices,default=ProductStatusType.draft.value)


    class Meta:
        ordering= ["-created_date"]

    def __str__(self):
        return self.title
    
    def get_price(self):
        discount_amount=self.price*Decimal(self.discount_price/100)
        discounted_amount=self.price-discount_amount
        return round(discounted_amount)
    

    def is_dicounted(self):
        return self.discount_price !=0



class ProductImageModel(models.Model):
    product=models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    file=models.ImageField(upload_to="product/extra-img/")
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
