import unittest

from user_service import UserService
from billing_service import BillingService
from cart_service import CartService


class TestServices(unittest.TestCase):

    def setUp(self):
        self.user_service = UserService()
        self.billing_service = BillingService()
        self.cart_service = CartService()

    def test_user_service(self):
        # Add user
        self.user_service.add_user("john", "john@example.com")

        # Try adding existing user
        with self.assertRaises(ValueError):
            self.user_service.add_user("john", "newemail@example.com")
        with self.assertRaises(ValueError):
            self.user_service.update_user("hwat", "newemail@example.com")
        with self.assertRaises(ValueError):
            self.user_service.remove_user("hwat")

        # Remove user
        self.user_service.remove_user("john")


        # Check court (simple test)
        self.assertTrue(self.user_service.check_court("JOHN"))
        self.assertFalse(self.user_service.check_court("jane"))

        self.user_service.add_user("alice", "alice@example.com")
        self.user_service.update_user(username="alice", new_email="newmail@example.com")
        self.assertEqual(self.user_service.users["alice"]["email"], "newmail@example.com")

    def test_billing_service(self):
        # Add billing record
        self.billing_service.add_billing(100, "Rent")

        # Update billing record
        self.billing_service.update_billing(0, new_description="Utilities")
        self.assertEqual(self.billing_service.billing_records[0].get('description'), "Utilities")


        # Remove billing record
        self.billing_service.remove_billing(0)

        # Try removing invalid index
        with self.assertRaises(IndexError):
            self.billing_service.remove_billing(-1)
        with self.assertRaises(IndexError):
            self.billing_service.remove_billing(3)

        self.billing_service.add_billing(100, "Rent")
        self.billing_service.add_billing(200, "Utilities")

        self.billing_service.update_billing(0, new_amount=125)
        self.assertEqual(self.billing_service.billing_records[0]['amount'], 125)
        # Test removing the last item
        self.billing_service.remove_billing(1)
        self.assertEqual(len(self.billing_service.billing_records), 1)

        # Test removing the first item
        self.billing_service.remove_billing(0)
        self.assertEqual(len(self.billing_service.billing_records), 0)

        # Test removing an invalid index
        with self.assertRaises(IndexError):
            self.billing_service.remove_billing(2)

        # Test update billing on invalid index
        with self.assertRaises(IndexError):
            self.billing_service.update_billing(-1)
        with self.assertRaises(IndexError):
            self.billing_service.update_billing(10)

    def test_cart_service(self):
        # Add items to cart
        self.cart_service.add_item("Apple", 1.00)
        self.cart_service.add_item("Banana", 0.50)

        # Calculate total
        self.assertEqual(self.cart_service.calculate_total(), 1.50)

        # Reset cart
        self.cart_service.reset_cart()
        self.assertEqual(len(self.cart_service.cart_items), 0)

        self.cart_service.add_item("apple", 1.00)
        self.assertEqual(len(self.cart_service.cart_items), 1)
        self.assertEqual(self.cart_service.cart_items[0]["item"], "apple")
        self.assertEqual(self.cart_service.cart_items[0]["price"], 1.00)

        with self.assertRaises(IndexError):
            self.cart_service.remove_item(-1)

        self.cart_service.remove_item(0)


if __name__ == '__main__':
    unittest.main()
