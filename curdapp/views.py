from django.shortcuts import render
from curdapp.models import ProductData
from curdapp.forms import InsertingData,UpdateData,DeletingDataForm
from django.http.response import HttpResponse

def home(request):
    return render(request,'home.html')


def createview(request):
    if request.method=="POST":
            product_id=request.POST.get('product_id')
            product_name=request.POST.get('product_name')
            product_cost=request.POST.get('product_cost')
            product_class=request.POST.get('product_class')
            no_of_products=request.POST.get('no_of_products')
            customer_name = request.POST.get('customer_name')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            manufacture_date=request.POST.get('manufacture_date')
            expiry_date=request.POST.get('expiry_date')

            data=ProductData(
                product_id=product_id,
                product_name=product_name,
                product_cost=product_cost,
                product_class=product_class,
                no_of_products=no_of_products,
                customer_name=customer_name,
                mobile=mobile,
                email=email,
                manufacture_date=manufacture_date,
                expiry_date=expiry_date
            )
            data.save()
            return render(request, 'create.html')

    else:
        return render(request,'create.html')


def retriveview(request):
    data=ProductData.objects.all()
    return render(request,'retrive.html',{'pdata':data})


def updateview(request):
    if request.method=="POST":
            product_id=request.POST.get("product_id")
            product_cost=request.POST.get("product_cost")
            pro_id=ProductData.objects.filter(product_id=product_id)
            if not pro_id:
                return HttpResponse("Product is not availabel")
            else:
                pro_id.update(product_cost=product_cost)
                return render(request,'update.html')
    else:
        return render(request, 'update.html')


def deleteview(request):
    if request.method=="POST":
        product_id=request.POST.get("product_id")
        pro_id=ProductData.objects.filter(product_id=product_id)
        if not pro_id:
            return HttpResponse("Product is not availabel")
        else:
            pro_id.delete()
            return render(request,'delete.html')
    else:
        return render(request,'delete.html')