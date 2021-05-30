from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
from django.urls import reverse
from django.utils.text import slugify
from datetime import datetime
# Create your models here.

# Address
# 2.Product
# 3.Order
# 4.AddToCart
# 5.ProductOrder
# 6.WishList

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='address')
    mobile_no=models.CharField(max_length=12)
    Flat_No=models.CharField(max_length=10)
    Area_Colony=models.CharField(max_length=100)
    Landmark=models.TextField()
    Town_City=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    Pincode=models.CharField(max_length=6)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering=['Pincode','user']
    
    # def get_absolute_url(self):

    #     return reverse('shop:Address_list')
class Product(models.Model):
        product_name=models.CharField(max_length= 100)
        slug=models.SlugField(unique=True)
        product_discription=models.TextField()
        product_price=models.IntegerField()
        product_picture=models.ImageField(upload_to='images',blank = True,null = True)
        product_launch_date=models.DateTimeField(default=datetime.now())
        product_manufacturer=models.TextField()
        product_rating=models.IntegerField()


        def __str__(self):
            return self.product_name


        def save(self,*args,**kwargs):
            self.slug=slugify(self.product_name)
            super().save(*args,**kwargs)


	# def get_absolute_url(self):
	# 	return reverse('product:single',kwargs={'slug':self.slug},)


        class Meta():
            ordering=['product_name']
        
class Order(models.Model):
        
        user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
        order_date=models.DateTimeField(default=datetime.now())
        product=models.ManyToManyField(Product,related_name='orders',through='ProductOrder')

        def __str__(self):
            return self.user.username


	# def get_absolute_url(self):   
	# 	return reverse('app:myorder')


        class Meta():
            ordering=['order_date']





class ProductOrder(models.Model):
	order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='products')
	product=models.ForeignKey(Product,on_delete=models.CASCADE)


	def __str__(self):
		return str(self.order.user.username)



class AddCart(models.Model):
	product=models.ForeignKey(Product,related_name='cart',on_delete=models.CASCADE)
	user=models.ForeignKey(User,related_name='cart',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.product)



	# def get_absolute_url(self):
	# 	return reverse('order:succe',kwargs={'pk':self.pk})


	class Meta():
		ordering=['user']


# class WishList(models.Model):
#     product=models.ForeignKey(Product,related_name='cart',on_delete=models.CASCADE)
#     user=models.ForeignKey(User,related_name='cart',on_delete=models.CASCADE)
    
