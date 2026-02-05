from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from apps.products.models import Category, Product
from apps.stores.models import Store, Inventory
from apps.orders.models import Order


class BasicProjectTests(TestCase):
    def setUp(self):
        self.client = Client()

        # Create admin user
        self.admin_user = User.objects.create_superuser(
            username="admin",
            password="admin123",
            email="admin@test.com"
        )

        # Create sample category and product
        self.category = Category.objects.create(name="Groceries")
        self.product = Product.objects.create(
            title="Rice",
            price=50,
            category=self.category
        )

        # Create store and inventory
        self.store = Store.objects.create(name="Main Store")
        self.inventory = Inventory.objects.create(
            store=self.store,
            product=self.product,
            quantity=100
        )

    # 1. Test admin login page loads
    def test_admin_login_page_loads(self):
        response = self.client.get("/admin/login/")
        self.assertEqual(response.status_code, 200)

    # 2. Test models were created correctly
    def test_models_creation(self):
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Store.objects.count(), 1)
        self.assertEqual(Inventory.objects.count(), 1)

    # 3️. Test order creation in DB
    def test_order_model_creation(self):
        order = Order.objects.create(store=self.store)
        self.assertIsNotNone(order.id)

    # 4️. Test order creation API endpoint exists
    def test_order_create_api_exists(self):
        response = self.client.get("/orders/create/")
        self.assertIn(response.status_code, [200, 405])

    # 5. Test homepage or root does not crash
    def test_root_url_response(self):
        response = self.client.get("/")
        self.assertIn(response.status_code, [200, 404])
