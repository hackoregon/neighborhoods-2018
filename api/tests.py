from django.test import TestCase, SimpleTestCase, TransactionTestCase
# from api.models import preexisting_models <-- this needs to be configured for our repo.


# Django, Writing and Running Unit Tests: https://docs.djangoproject.com/en/2.0/topics/testing/overview/
# Django, Automated Unit Testing Tutorial: https://docs.djangoproject.com/en/2.0/intro/tutorial05/

class ExampleTestCase(TestCase):
    def setUp(self):
        pass

    def test_example(self):
        self.assertTrue(True)

class ExampleModelTestCase(TestCase):
    def setUp(self):
        pass

    def test_model(self):
        self.assertTrue(True)


# https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.SimpleTestCase
class ExampleSimpleTestCase(SimpleTestCase):
    def test_simple_example(self):
        self.assertTrue(True)

# https://docs.djangoproject.com/en/2.0/topics/testing/tools/#transactiontestcase
class ExampleTransactionTestCase(TransactionTestCase):
    def test_transaction_example(self):
        self.assertTrue(True)

# Create your tests here.
