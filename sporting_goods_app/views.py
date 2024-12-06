from django.shortcuts import render

from django.http import JsonResponse
from .repositories import ProductRepository, InventoryRepository

def product_list(request):
    products = ProductRepository.get_all_products()
    products_data = [{"id": product.id, "name": product.product_name} for product in products]
    return JsonResponse(products_data, safe=False)

def product_detail(request, product_id):
    product = ProductRepository.get_product_by_id(product_id)
    if product:
        product_data = {
            "id": product.id,
            "name": product.product_name,
            "price": product.price,
            "description": product.description
        }
        return JsonResponse(product_data)
    else:
        return JsonResponse({"error": "Product not found"}, status=404)

