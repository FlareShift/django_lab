from .models import Product, Inventory, Supplier

class ProductRepository:
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_product_by_id(product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    @staticmethod
    def create_product(data):
        product = Product(**data)
        product.save()
        return product

class InventoryRepository:
    @staticmethod
    def get_inventory_by_product(product_id):
        try:
            return Inventory.objects.get(product_id=product_id)
        except Inventory.DoesNotExist:
            return None

class SupplierRepository:
    @staticmethod
    def get_supplier_by_id(supplier_id):
        try:
            return Supplier.objects.get(id=supplier_id)
        except Supplier.DoesNotExist:
            return None
