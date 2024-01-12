from django.core.management.base import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    """
    Creates products
    """
    def handle(self, *args, **options):
        self.stdout.write("Creating products")
        product_names = [
            "Laptop",
            "Desktop",
            "Smartphone",
        ]
        for product_name in product_names:
            product, create = Product.objects.get_or_create(name=product_name)
            self.stdout.write(f"Created product {product_name}")
        self.stdout.write(self.style.SUCCESS("Products created"))


