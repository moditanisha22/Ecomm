from django.contrib.auth import login
from django.db import models
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from . import Checksum
# Create your views here.
MERCHANT_KEY="P1ZLXK_oh0S_C1zu"
from .models import *
class Product_List(ListView):
    model=Product
    template_name='shop/product_list.html'
    context_object_name='list_item'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jeans']=Product.objects.filter(product_name__icontains='jeans')
        context['shirt']=Product.objects.filter(product_name__icontains='shirt')[:3]
        context['top']=Product.objects.filter(product_name__icontains='top')[:3]
        
        return context

def addtocart(request,slug):
        if(not(request.user.is_authenticated)):
            return redirect("account:login")
        else:
            product=get_object_or_404(Product,slug=slug)
            
            
            addcart=AddCart.objects.filter(user=request.user,product=product)
            if addcart:
                return redirect('shop:cartlist')
            else:
        
                AddCart.objects.create(user=request.user,product=product)
        
            return redirect('shop:cartlist')

class cartlist(ListView):
    model=AddCart
    template_name='shop/add_to_cart.html'


# def AddToCart(request,pk):

# 	product=get_object_or_404(Product,pk=pk)
# 	print(product)
# 	try:
# 		AddCart.objects.create(user=request.user,product=product)

# 	except:
# 		messages.warning(request,'Please Login')
# 		redirect('account:login')

# 	else:
# 		messages.success(request,'your paroduct is saved in cart')

# 	return redirect('app:cartlist')
@login_required
def remove_product_from_cart(request,slug):
    product=get_object_or_404(Product,slug=slug)
    addcart=get_object_or_404(AddCart,user=request.user,product=product)
    addcart.delete()
    return redirect('shop:cartlist')

def CreateProduct(request,slug):
    if(not(request.user.is_authenticated)):
            return redirect("account:login")
    else:
        order=Order(user=request.user,order_date=datetime.now())
        order.save()
        product=get_object_or_404(Product,slug=slug)
        param_dict={
        
        "MID": "bENzWU52249925662751",
        "ORDER_ID": str(order.pk),
        "CUST_ID": "tanisha.modi.23@gmail.com",
        "TXN_AMOUNT": str(product.product_price),
        "CHANNEL_ID": "WEB",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "WEBSTAGING",
        'CALLBACK_URL':f"http://127.0.0.1:8000/final_order/{slug}/{order.pk}"
        }
        param_dict['CHECKSUMHASH']=Checksum.generate_checksum(param_dict,MERCHANT_KEY)
        return render(request,'shop/paytm.html',{'param_dict':param_dict})
        # product=get_object_or_404(Product,slug=slug)
        # return render(request,'shop/order.html',{'product':product})
       

class OrderList(TemplateView):
    template_name='shop/order_list.html'
@login_required
def CancelOrder(request,slug,pk):
    product=get_object_or_404(Product,slug=slug)
    order=get_object_or_404(Order,pk=pk)
    order_product=ProductOrder.objects.filter(order=order,product=product)
    if order_product:
        order_product.delete()
        order.delete()
        return redirect("shop:order_list")
    else:
        return redirect("shop:order_list")
def searchquery(request):
    if request.method=='GET':
        query=request.GET['product']
        product_list=Product.objects.filter(product_name__icontains=query)
        return render(request,'shop/product_list.html',{'list':product_list})

@csrf_exempt
def final_order(request,slug,pk):
        form=request.POST
        response_dict={}
        for i in form.keys():
            response_dict[i]=form[i]
            if i=='CHECKSUMHASH':
                checksum=form[i]
        verify=Checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)
        if verify:
            if response_dict['RESPCODE'] =='01':
                print("order success full")
                product=get_object_or_404(Product,slug=slug)
               
                order=get_object_or_404(Order,pk=pk)
                ProductOrder.objects.create(product=product,order=order)
                
            else:
                print("not successful" + response_dict['RESPMSG'])
        product_list=Product.objects.all()
        return redirect('shop:order_list')
    # product=get_object_or_404(Product,slug=slug)
    # order=get_object_or_404(Order,pk=pk)
    # try:
    #     ProductOrder.objects.create(order=order,product=product)
       
    # except Exception as e:
    #     print("sorry we are not creating any object")
    # return redirect('shop:order_list')
