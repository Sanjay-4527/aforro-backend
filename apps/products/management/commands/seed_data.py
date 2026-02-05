from django.core.management.base import BaseCommand
from apps.products.models import Category, Product

class Command(BaseCommand):
    help = "Seed initial product data"

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(
            name="Groceries"
        )

        Product.objects.get_or_create(
            title="Apple",
            category=category,
            price=10.0,
            description="Fresh red apple"
        )

        Product.objects.get_or_create(
            title="Milk",
            category=category,
            price=25.0,
            description="Dairy milk packet"
        )

        self.stdout.write(self.style.SUCCESS("Seed data created successfully"))

