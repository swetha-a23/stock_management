import unittest
from unittest.mock import MagicMock
from datetime import datetime
from testfixtures import compare
from testfixtures import TempDirectory

from models import *
from database import db_session
from dao import *
from resolvers import *
   

class TestSupplierResolvers(unittest.TestCase):
    def setUp(self):
        self.supplier_id = 1
        self.supplier_name = "Supplier 1"
        self.supplier_address = "Address 1"
        self.contact_number = "1234567890"

    def test_resolve_get_supplier_by_id(self):
        supplier = Supplier(
            supplier_id=self.supplier_id,
            supplier_name=self.supplier_name,
            supplier_address=self.supplier_address,
            contact_number=self.contact_number,
        )
        db_session.query = MagicMock(return_value=supplier)

        result = resolve_get_supplier_by_id(None, None, self.supplier_id)
        compare(result, supplier)

    def test_resolve_get_all_suppliers(self):
        suppliers = [
            Supplier(
                supplier_id=1,
                supplier_name="Supplier 1",
                supplier_address="Address 1",
                contact_number="1234567890",
            ),
            Supplier(
                supplier_id=2,
                supplier_name="Supplier 2",
                supplier_address="Address 2",
                contact_number="9876543210",
            ),
        ]
        db_session.query = MagicMock(return_value=suppliers)

        result = resolve_get_all_suppliers(None, None)
        compare(result, suppliers)

    def test_resolve_create_supplier(self):
        supplier = Supplier(
            supplier_id=self.supplier_id,
            supplier_name=self.supplier_name,
            supplier_address=self.supplier_address,
            contact_number=self.contact_number,
        )
        db_session.add = MagicMock()
        db_session.commit = MagicMock()
        create_supplier.return_value = supplier

        result = resolve_create_supplier(None, None, self.supplier_name, self.supplier_address, self.contact_number)
        compare(result, supplier)
        create_supplier.assert_called_with(
            self.supplier_name, self.supplier_address, self.contact_number
        )
        db_session.add.assert_called_with(supplier)
        db_session.commit.assert_called()

    def test_resolve_update_supplier(self):
        supplier = Supplier(
            supplier_id=self.supplier_id,
            supplier_name=self.supplier_name,
            supplier_address=self.supplier_address,
            contact_number=self.contact_number,
        )
        db_session.query = MagicMock(return_value=supplier)
        db_session.commit = MagicMock()

        result = resolve_update_supplier(
            None, None, self.supplier_id, self.supplier_name, self.supplier_address, self.contact_number
        )
        compare(result, supplier)
        db_session.commit.assert_called()

    def test_resolve_delete_supplier(self):
        supplier = Supplier(
            supplier_id=self.supplier_id,
            supplier_name=self.supplier_name,
            supplier_address=self.supplier_address,
            contact_number=self.contact_number,
        )
        db_session.query = MagicMock(return_value=supplier)
        db_session.delete = MagicMock()
        db_session.commit = MagicMock()

        result = resolve_delete_supplier(None, None, self.supplier_id)
        compare(result, supplier)
        db_session.delete.assert_called_with(supplier)
        db_session.commit.assert_called()




class TestStockResolvers(unittest.TestCase):
    def setUp(self):
        self.stock_id = 1
        self.product_id = 1
        self.quantity = 10
        self.location = "Location 1"

    def test_resolve_get_stock_by_id(self):
        stock = Stock(
            stock_id=self.stock_id,
            product_id=self.product_id,
            quantity=self.quantity,
            location=self.location,
        )
        db_session.query = MagicMock(return_value=stock)

        result = resolve_get_stock_by_id(None, None, self.stock_id)
        compare(result, stock)

    def test_resolve_get_all_stock(self):
        stocks = [
            Stock(stock_id=1, product_id=1, quantity=10, location="Location 1"),
            Stock(stock_id=2, product_id=2, quantity=5, location="Location 2"),
        ]
        db_session.query = MagicMock(return_value=stocks)

        result = resolve_get_all_stock(None, None)
        compare(result, stocks)

    def test_resolve_create_stock(self):
        stock = Stock(
            stock_id=self.stock_id,
            product_id=self.product_id,
            quantity=self.quantity,
            location=self.location,
        )
        db_session.add = MagicMock()
        db_session.commit = MagicMock()
        create_stock.return_value = stock

        result = resolve_create_stock(None, None, self.product_id, self.quantity, self.location)
        compare(result, stock)
        create_stock.assert_called_with(self.product_id, self.quantity, self.location)
        db_session.add.assert_called_with(stock)
        db_session.commit.assert_called()

    def test_resolve_update_stock(self):
        stock = Stock(
            stock_id=self.stock_id,
            product_id=self.product_id,
            quantity=self.quantity,
            location=self.location,
        )
        db_session.query = MagicMock(return_value=stock)
        db_session.commit = MagicMock()

        result = resolve_update_stock(
            None, None, self.stock_id, self.product_id, self.quantity, self.location
        )
        compare(result, stock)
        db_session.commit.assert_called()

    def test_resolve_delete_stock(self):
        stock = Stock(
            stock_id=self.stock_id,
            product_id=self.product_id,
            quantity=self.quantity,
            location=self.location,
        )
        db_session.query = MagicMock(return_value=stock)
        db_session.delete = MagicMock()
        db_session.commit = MagicMock()

        result = resolve_delete_stock(None, None, self.stock_id)
        compare(result, stock)
        db_session.delete.assert_called_with(stock)
        db_session.commit.assert_called()

class TestConsumerResolvers(unittest.TestCase):
    def setUp(self):
        self.consumer_id = 1
        self.consumer_name = "Consumer 1"
        self.consumer_address = "Address 1"
        self.contact_number = "1234567890"

    def test_resolve_get_consumer_by_id(self):
        consumer = Consumer(
            consumer_id=self.consumer_id,
            consumer_name=self.consumer_name,
            consumer_address=self.consumer_address,
            contact_number=self.contact_number,
        )
        db_session.query = MagicMock(return_value=consumer)

        result = resolve_get_consumer_by_id(None, None, self.consumer_id)
        compare(result, consumer)

    def test_resolve_get_all_consumers(self):
        consumers = [
            Consumer(
                consumer_id=1,
                consumer_name="Consumer 1",
                consumer_address="Address 1",
                contact_number="1234567890",
            ),
            Consumer(
                consumer_id=2,
                consumer_name="Consumer 2",
                consumer_address="Address 2",
                contact_number="9876543210",
            ),
        ]
        db_session.query = MagicMock(return_value=consumers)

        result = resolve_get_all_consumers(None, None)
        compare(result, consumers)

    def test_resolve_create_consumer(self):
        consumer = Consumer(
            consumer_id=self.consumer_id,
            consumer_name=self.consumer_name,
            consumer_address=self.consumer_address,
            contact_number=self.contact_number,
        )
        db_session.add = MagicMock()
        db_session.commit = MagicMock()
        create_consumer.return_value = consumer

        result = resolve_create_consumer(None, None, self.consumer_name, self.consumer_address, self.contact_number)
        compare(result, consumer)
        create_consumer.assert_called_with(
            self.consumer_name, self.consumer_address, self.contact_number
        )
        db_session.add.assert_called_with(consumer)
        db_session.commit.assert_called()

    def test_resolve_update_consumer(self):
        consumer = Consumer(
            consumer_id=self.consumer_id,
            consumer_name=self.consumer_name,
            consumer_address=self.consumer_address,
            contact_number=self.contact_number,
        )
        db_session.query = MagicMock(return_value=consumer)
        db_session.commit = MagicMock()

        result = resolve_update_consumer(
            None, None, self.consumer_id, self.consumer_name, self.consumer_address, self.contact_number
        )
        compare(result, consumer)
        db_session.commit.assert_called()

    def test_resolve_delete_consumer(self):
        consumer = Consumer(
            consumer_id=self.consumer_id,
            consumer_name=self.consumer_name,
            consumer_address=self.consumer_address,
            contact_number=self.contact_number,
        )
        db_session.query = MagicMock(return_value=consumer)
        db_session.delete = MagicMock()
        db_session.commit = MagicMock()

        result = resolve_delete_consumer(None, None, self.consumer_id)
        compare(result, consumer)
        db_session.delete.assert_called_with(consumer)
        db_session.commit.assert_called()

class TestProductResolvers(unittest.TestCase):
    def setUp(self):
        self.product_id = 1
        self.product_name = "Product 1"
        self.amount = 10.99
        self.description = "Description 1"

    def test_resolve_get_product_by_id(self):
        product = Product(
            product_id=self.product_id,
            product_name=self.product_name,
            amount=self.amount,
            description=self.description,
        )
        db_session.query = MagicMock(return_value=product)

        result = resolve_get_product_by_id(None, None, self.product_id)
        compare(result, product)

    def test_resolve_get_all_products(self):
        products = [
            Product(
                product_id=1,
                product_name="Product 1",
                amount=10.99,
                description="Description 1",
            ),
            Product(
                product_id=2,
                product_name="Product 2",
                amount=15.99,
                description="Description 2",
            ),
        ]
        db_session.query = MagicMock(return_value=products)

        result = resolve_get_all_products(None, None)
        compare(result, products)

    def test_resolve_create_product(self):
        product = Product(
            product_id=self.product_id,
            product_name=self.product_name,
            amount=self.amount,
            description=self.description,
        )
        db_session.add = MagicMock()
        db_session.commit = MagicMock()
        create_product.return_value = product

        result = resolve_create_product(
            None, None, self.product_name, self.amount, self.description
        )
        compare(result, product)
        create_product.assert_called_with(
            self.product_name, self.amount, self.description
        )
        db_session.add.assert_called_with(product)
        db_session.commit.assert_called()

    def test_resolve_update_product(self):
        product = Product(
            product_id=self.product_id,
            product_name=self.product_name,
            amount=self.amount,
            description=self.description,
        )
        db_session.query = MagicMock(return_value=product)
        db_session.commit = MagicMock()

        result = resolve_update_product(
            None,
            None,
            self.product_id,
            self.product_name,
            self.amount,
            self.description,
        )
        compare(result, product)
        db_session.commit.assert_called()

    def test_resolve_delete_product(self):
        product = Product(
            product_id=self.product_id,
            product_name=self.product_name,
            amount=self.amount,
            description=self.description,
        )
        db_session.query = MagicMock(return_value=product)
        db_session.delete = MagicMock()
        db_session.commit = MagicMock()

        result = resolve_delete_product(None, None, self.product_id)
        compare(result, product)
        db_session.delete.assert_called_with(product)
        db_session.commit.assert_called()


if __name__ == "__main__":
    unittest.main()
