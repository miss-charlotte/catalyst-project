from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Sale
from .forms import SellForm, AddForm
from django.db import models
from .filters import Product_filter
from django.db.models import Count
import datetime
# Create your views here.
# @login_required

def about(request):
    return render(request, 'products/about.html') 
  
def index(request):
    products = Product.objects.all()
    num_customers = Sale.objects.values('boughtBy').distinct().count()
    num_out_of_stock = Product.objects.filter(quantityinStore=0).count()
    num_in_store = Product.objects.aggregate(total_quantity=models.Sum('quantityinStore'))['total_quantity']
    expired_products = Product.objects.filter(expiryDate__lte=datetime.date.today())
    num_expired_quantity = sum([product.expiredQuantity for product in expired_products])
    context = {
        'products': products,
        'num_customers': num_customers,
        'num_out_of_stock':num_out_of_stock,
        'num_in_store': num_in_store,
        'num_expired_quantity': num_expired_quantity,
    }
    return render(request, 'products/index.html', context)


def medicine(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'products/medicine.html', {'products': products})


def medicine(request):
    products = Product.objects.all().order_by('-id')
    product_filters = Product_filter(request.GET,queryset = products)
    products = product_filters.qs
    return render(request, 'products/medicine.html', {'products':products, 'product_filters': product_filters})


def product_detail(request, product_id):
    product = Product.objects.get(id= product_id)
    return render(request, 'products/product_detail.html', {'product': product}) 
   

def sales(request):
    sales = Sale.objects.all()  
    total = sum([medicines.amountPaid for medicines in sales])
    change = sum([medicines.getChange() for medicines in sales])
    #count the number of cutomers who have made a purchase
    num_customers = Sale.objects.annotate(num_sales=Count('boughtBy', distinct=True)).aggregate(total_customers=Count('num_sales'))['total_customers']
    net = total - change
    return render(request, 'products/sales.html',{
        'sales': sales,
        'total': total,
        'change': change,
        'net': net,
        'num_customers': num_customers
    })



def receipts(request):
     sales =Sale.objects.all().order_by('-id')
     return render(request, 'products/receipts.html', {'sales': sales})

def final_receipt(request, receipts_id):
    receipts = Sale.objects.get(id=receipts_id)
    return render(request, 'products/final_receipt.html', {'receipts':receipts})

def sell_item(request, pk):
    soldMedicine= Product.objects.get(id=pk)
    salesForm=SellForm(request.POST)

    if request.method =='POST':
        if salesForm.is_valid():
            newSale = salesForm.save(commit = False)
            newSale.medicine =soldMedicine
            newSale.unitCost =soldMedicine.unitCost
            newSale.save()
            #to keep track of the stock remaining after sales
            quantitySold =int(request.POST['quantity'])
            soldMedicine.quantityinStore -= quantitySold
            soldMedicine.save()
            print(soldMedicine.medicineName)
            print(request.POST['quantity'])
            print(soldMedicine.quantityinStore)

            return redirect('receipts')
    return render(request, 'products/sell_item.html', {'salesForm': salesForm})

def add_to_stock(request, pk):
    soldMedicine =Product.objects.get(id =pk)
    form =AddForm(request.POST)

    if request.method =='POST':
        if form.is_valid():
            addQuantity =int(request.POST['receivedQuantity'])
            soldMedicine.quantityinStore += addQuantity
            soldMedicine.save()
            #to add to the remaining stock, quantity is reducing
            print(addQuantity)
            print(soldMedicine.quantityinStore)

            return redirect('medicine')
    return render (request, 'products/add_to_stock.html', {'form':form}) 


def delete(request, pk):
  products = Product.objects.get(id=pk)
  products.delete()
  return render (request, 'products/medicine.html')

