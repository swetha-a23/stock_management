from models import Supplier, Stock, Consumer, Product, SupplierOrder, ConsumerOrder, SupplierTransaction, ConsumerTransaction
from database import session
from sqlalchemy.orm import joinedload

import re

from schemas import StockSchema

class SupplierDAO:
    @staticmethod
    def get_supplier_by_id(supplier_id):
        return session.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()
    
    @staticmethod
    def get_all_suppliers():
        return session.query(Supplier).all()
    
    @staticmethod
    def create_supplier(supplier_name, supplier_address, contact_number):
        # Validate contact_number using a regular expression
        if not re.match(r'^\d{10}$', str(contact_number)):
            raise ValueError("Invalid contact number")

        supplier = Supplier(supplier_name=supplier_name, supplier_address=supplier_address, contact_number=contact_number)
        session.add(supplier)
        session.commit()
        return supplier
    @staticmethod
    def update_supplier(supplier_id, supplier_name, supplier_address, contact_number):
        supplier = SupplierDAO.get_supplier_by_id(supplier_id)
        if supplier:
            supplier.supplier_name = supplier_name
            supplier.supplier_address = supplier_address
            supplier.contact_number = contact_number
            session.commit()
        return supplier
    
    @staticmethod
    def delete_supplier(supplier_id):
        supplier = SupplierDAO.get_supplier_by_id(supplier_id)
        if supplier:
            session.delete(supplier)
            session.commit()
        return supplier

class StockDAO:
    @staticmethod
    def get_stock_by_id(stock_id):
        return session.query(Stock).filter(Stock.stock_id == stock_id).first()
    
    @staticmethod
    def get_all_stock():
        return session.query(Stock).all()

    @staticmethod
    def create_stock(product_id, quantity, location):

        stock = Stock(product_id=product_id, quantity=quantity, location=location)
        session.add(stock)
        session.commit()
        return stock
    
    @staticmethod
    def create_stock(product_id, quantity, location):
        stock = Stock(product_id=product_id, quantity=quantity, location=location)
        session.add(stock)
        session.commit()
        
        stock_schema = StockSchema(
            stock_id=stock.stock_id,
            product_id=stock.product_id,
            quantity=stock.quantity,
            location=stock.location
        )
        
        return stock_schema

    @staticmethod
    def update_stock(stock_id, product_id, quantity, location):
        stock = StockDAO.get_stock_by_id(stock_id)
        if stock:
            stock.product_id = product_id
            stock.quantity = quantity
            stock.location = location
            session.commit()
        return stock
    
    @staticmethod
    def delete_stock(stock_id):
        stock = StockDAO.get_stock_by_id(stock_id)
        if stock:
            session.delete(stock)
            session.commit()
        return stock

class ConsumerDAO:

    @staticmethod
    def get_consumer_by_id(consumer_id):
        return session.query(Consumer).filter(Consumer.consumer_id == consumer_id).first()
    
    @staticmethod
    def get_all_consumers():
        return session.query(Consumer).all()
    
    @staticmethod
    def create_consumer(consumer_name, consumer_address, contact_number):
        # Validate contact_number using a regular expression
        if not re.match(r'^\d{10}$', str(contact_number)):
            raise ValueError("Invalid contact number")

        consumer = Consumer(consumer_name=consumer_name, consumer_address=consumer_address, contact_number=contact_number)
        session.add(consumer)
        session.commit()
        return consumer
    
    @staticmethod
    def update_consumer(consumer_id, consumer_name, consumer_address, contact_number):
        consumer = ConsumerDAO.get_consumer_by_id(consumer_id)
        if consumer:
            consumer.consumer_name = consumer_name
            consumer.consumer_address = consumer_address
            consumer.contact_number = contact_number
            session.commit()
        return consumer
    
    @staticmethod
    def delete_consumer(consumer_id):
        consumer = ConsumerDAO.get_consumer_by_id(consumer_id)
        if consumer:
            session.delete(consumer)
            session.commit()
        return consumer

class ProductDAO:

    @staticmethod 
    def get_product_by_id(product_id):
        return session.query(Product).filter(Product.product_id == product_id).first()

    @staticmethod
    def get_all_products():
        return session.query(Product).all()
    
    @staticmethod
    def create_product(product_name, amount, description):
        # Validate product_name using a regular expression
        if not re.match(r'^[A-Za-z0-9\s]+$', product_name):
            raise ValueError("Invalid product name")

        product = Product(product_name=product_name, amount=amount, description=description)
        session.add(product)
        session.commit()
        return product
    
    @staticmethod
    def update_product(product_id, product_name, amount, description):
        product = ProductDAO.get_product_by_id(product_id)
        if product:
            product.product_name = product_name
            product.amount = amount
            product.description = description
            session.commit()
        return product
    
    @staticmethod
    def delete_product(product_id):
        product = ProductDAO.get_product_by_id(product_id)
        if product:
            session.delete(product)
            session.commit()
        return product

class SupplierOrderDAO:

    @staticmethod
    def get_supplier_order_by_id(order_id):
        print(session.query(SupplierOrder).filter(SupplierOrder.order_id == order_id).first())
        return session.query(SupplierOrder).filter(SupplierOrder.order_id == order_id).first()
    
    @staticmethod
    def get_all_supplier_orders():
        return session.query(SupplierOrder).all()
    
    @staticmethod
    def create_supplier_order(supplier_id, stock_id, order_date, quantity):
        product = SupplierOrderDAO.get_product_by_id(stock_id)
        if not product:
            raise ValueError("Product not found")

        total_amount = quantity * product.amount
        supplier_order = SupplierOrder(
            supplier_id=supplier_id,
            stock_id=stock_id,
            order_date=order_date,
            quantity=quantity,
            total_amount=total_amount
        )
        session.add(supplier_order)
        session.commit()
        return supplier_order
    
    @staticmethod
    def update_supplier_order(order_id, supplier_id, stock_id, order_date, quantity):
        supplier_order = SupplierOrderDAO.get_supplier_order_by_id(order_id)
        if supplier_order:
            supplier_order.supplier_id = supplier_id
            supplier_order.stock_id = stock_id
            supplier_order.order_date = order_date
            supplier_order.quantity = quantity
            supplier_order.calculate_total_price()
            session.commit()
        return supplier_order
    
    @staticmethod
    def delete_supplier_order(order_id):
        supplier_order = SupplierOrderDAO.get_supplier_order_by_id(order_id)
        if supplier_order:
            session.delete(supplier_order)
            session.commit()
        return supplier_order

class ConsumerOrderDAO:

    @staticmethod   
    def get_consumer_order_by_id(order_id):
        return session.query(ConsumerOrder).filter(ConsumerOrder.order_id == order_id).first()
    
    @staticmethod
    def get_all_consumer_orders():
        return session.query(ConsumerOrder).all()
    
    @staticmethod
    def create_consumer_order(consumer_id, product_id, order_date, quantity):
        product = ConsumerOrderDAO.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found")

        total_amount = quantity * product.amount
        consumer_order = ConsumerOrder(
            consumer_id=consumer_id,
            product_id=product_id,
            order_date=order_date,
            quantity=quantity,
            total_amount=total_amount
        )
        session.add(consumer_order)
        session.commit()
        return consumer_order
    
    @staticmethod
    def update_consumer_order(order_id, consumer_id, product_id, order_date, quantity):
        consumer_order = ConsumerOrderDAO.get_consumer_order_by_id(order_id)
        if consumer_order:
            consumer_order.consumer_id = consumer_id
            consumer_order.product_id = product_id
            consumer_order.order_date = order_date
            consumer_order.quantity = quantity
            consumer_order.calculate_total_price()
            session.commit()
        return consumer_order
    
    @staticmethod
    def delete_consumer_order(order_id):
        consumer_order = ConsumerOrderDAO.get_consumer_order_by_id(order_id)
        if consumer_order:
            session.delete(consumer_order)
            session.commit()
        return consumer_order

class SupplierTransactionDAO:

    @staticmethod   
    def get_supplier_transaction_by_id(transaction_id):
        return session.query(SupplierTransaction).filter(SupplierTransaction.transaction_id == transaction_id).first()
    
    @staticmethod
    def get_all_supplier_transactions():
        return session.query(SupplierTransaction).all()
    
    @staticmethod
    def create_supplier_transaction(order_id, supplier_id,  transaction_date):
        supplier = SupplierTransactionDAO.get_supplier_by_id(supplier_id)
        order = SupplierTransactionDAO.get_supplier_order_by_id(order_id)
        if supplier and order:
            supplier_transaction = SupplierTransaction(
                supplier_id=supplier_id,
                order_id=order_id,
                transaction_date=transaction_date
            )
            supplier_transaction.amount = order.total_amount

            session.add(supplier_transaction)
            session.commit()
            return supplier_transaction
        else:
            return None
        
    @staticmethod
    def update_supplier_transaction(transaction_id, supplier_id, order_id, transaction_date):
        supplier_transaction = SupplierTransactionDAO.get_supplier_transaction_by_id(transaction_id)
        if supplier_transaction:
            supplier_transaction.supplier_id = supplier_id
            supplier_transaction.order_id = order_id
            supplier_transaction.transaction_date = transaction_date
            supplier_transaction.set_amount_from_order()  

            session.commit()
        return supplier_transaction
    
    @staticmethod
    def delete_supplier_transaction(transaction_id):
        supplier_transaction = SupplierTransactionDAO.get_supplier_transaction_by_id(transaction_id)
        if supplier_transaction:
            session.delete(supplier_transaction)
            session.commit()
        return supplier_transaction

class ConsumerTransactionDAO:

    @staticmethod
    def get_consumer_transaction_by_id(transaction_id):
        return session.query(ConsumerTransaction).filter(ConsumerTransaction.transaction_id == transaction_id).first()
    
    @staticmethod
    def get_all_consumer_transactions():
        return session.query(ConsumerTransaction).all()
    
    @staticmethod
    def create_consumer_transaction(consumer_id, order_id, stock_id, transaction_date):
        consumer = ConsumerTransactionDAO.get_consumer_by_id(consumer_id)
        order = ConsumerTransactionDAO.get_consumer_order_by_id(order_id)
        stock = ConsumerTransactionDAO.get_stock_by_id(stock_id)
        if consumer and order and stock:
            total_amount = order.total_amount  
            transaction = ConsumerTransaction(
                consumer_id=consumer_id,
                order_id=order_id,
                stock_id=stock_id,
                transaction_date=transaction_date,
                amount=total_amount  
            )
            session.add(transaction)
            session.commit()
            return transaction
        else:
            return None
        
    @staticmethod
    def update_consumer_transaction(transaction_id, amount=None, transaction_date=None):
        transaction = ConsumerTransactionDAO.get_consumer_transaction_by_id(transaction_id)
        if transaction:
            if amount is not None:
                transaction.amount = amount
            if transaction_date:
                transaction.transaction_date = transaction_date
            session.commit()
        return transaction
    
    @staticmethod
    def delete_consumer_transaction(transaction_id):
        consumer_transaction = ConsumerTransactionDAO.get_consumer_transaction_by_id(transaction_id)
        if consumer_transaction:
            session.delete(consumer_transaction)
            session.commit()
        return consumer_transaction
