from django.core.management.base import BaseCommand

from products.models import Product, Category

class Command(BaseCommand):
    help = 'Add products to the database'

    Product.objects.all().delete()
    Category.objects.all().delete()

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(first_name='Овощи',description='полезные овощные культуры')

        products = [
            {'first_name': 'Картофель', 'description': 'новый урожай 2025 года','category': category,'price': 69.98},
            {'first_name': 'Морковь', 'description': 'полезна для зрения','category': category,'price': 38},
        ]
        for products_data in products:
            product, created = Product.objects.get_or_create(**products_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added products: {product.first_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'product already exist: {product.first_name}'))
