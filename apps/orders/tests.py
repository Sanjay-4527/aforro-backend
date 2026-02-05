from django.test import TestCase, Client

class OrderTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_order(self):
        response = self.client.get("/orders/create/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("task_id", response.json())

    def test_admin_login_page(self):
        response = self.client.get("/admin/login/")
        self.assertEqual(response.status_code, 200)
