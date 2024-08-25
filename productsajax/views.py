from django.shortcuts import render
from products.models import MedicalProduct
from medicalproductsapi.serializers import ProductSerializer
from django.http import JsonResponse
from rest_framework import status
from products.forms import ProductForm


def listtemplate(request):
    return render(request,'ajax.html')

def list_products(request):
    product_list = MedicalProduct.objects.all().values()
    serializer = ProductSerializer(product_list, many=True)
    return JsonResponse(serializer.data, safe=False)


def create_products(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save()
        return JsonResponse({'id': product.id}, status=status.HTTP_201_CREATED)
    return JsonResponse(form.errors, status=status.HTTP_400_BAD_REQUEST)

from products.models import MedicalProduct
from medicalproductsapi.serializers import ProductSerializer
from django.http import JsonResponse
from rest_framework import status


def get_products(request):
    product_id = request.GET.get('productId')
    product = MedicalProduct.objects.get(pk=product_id)
    serializer = ProductSerializer(product)
    return JsonResponse(serializer.data)

def update_products(request):
    if request.method == 'POST':
        product_id = request.POST.get('productId')
        product = MedicalProduct.objects.get(pk=product_id)
        serializer = ProductSerializer(product, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)
        
from products.models import MedicalProduct
from django.http import JsonResponse
from rest_framework import status

def delete_product(request):
    if request.method == "POST":
        product_id = request.POST.get('productId')
        print(product_id)
        try:
            product = MedicalProduct.objects.get(pk=product_id)
            product.delete()
            return JsonResponse({'status': 1})
        except MedicalProduct.DoesNotExist:
            return JsonResponse({'status': 0, 'message': 'Product does not exist'})
    else:
        return JsonResponse({'status': 0, 'message': 'Invalid request method'})