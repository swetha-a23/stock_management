from models import Supplier, Stock, Consumer, Product, SupplierOrder, ConsumerOrder, SupplierTransaction, ConsumerTransaction
from database import db_session
from sqlalchemy.orm import joinedload

import re

# DAO functions for Supplier
def get_supplier_by_id(supplier_id):
    return db_session.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()

def get_all_suppliers():
    return db_session.query(Supplier).all()

def create_supplier(supplier_name, supplier_address, contact_number):
    # Validate contact_number using a regular expression
    if not re.match(r'^\d{10}$', str(contact_number)):
        raise ValueError("Invalid contact number")

    supplier = Supplier(supplier_name=supplier_name, supplier_address=supplier_address, contact_number=contact_number)
    db_session.add(supplier)
    db_session.commit()
    return supplier

def update_supplier(supplier_id, supplier_name, supplier_address, contact_number):
    supplier = get_supplier_by_id(supplier_id)
    if supplier:
        supplier.supplier_name = supplier_name
        supplier.supplier_address = supplier_address
        supplier.contact_number = contact_number
        db_session.commit()
    return supplier

def delete_supplier(supplier_id):
    supplier = get_supplier_by_id(supplier_id)
    if supplier:
        db_session.delete(supplier)
        db_session.commit()
    return supplier

# DAO functions for Stock
def get_stock_by_id(stock_id):
    return db_session.query(Stock).filter(Stock.stock_id == stock_id).first()

def get_all_stock():
    return db_session.query(Stock).all()

def create_stock(product_id, quantity, location):

    stock = Stock(product_id=product_id, quantity=quantity, location=location)
    db_session.add(stock)
    db_session.commit()
    return stock

def update_stock(stock_id, product_id, quantity, location):
    stock = get_stock_by_id(stock_id)
    if stock:
        stock.product_id = product_id
        stock.quantity = quantity
        stock.location = location
        db_session.commit()
    return stock

def delete_stock(stock_id):
    stock = get_stock_by_id(stock_id)
    if stock:
        db_session.delete(stock)
        db_session.commit()
    return stock

# DAO functions for Consumer
def get_consumer_by_id(consumer_id):
    return db_session.query(Consumer).filter(Consumer.consumer_id == consumer_id).first()

def get_all_consumers():
    return db_session.query(Consumer).all()

def create_consumer(consumer_name, consumer_address, contact_number):
    # Validate contact_number using a regular expression
    if not re.match(r'^\d{10}$', str(contact_number)):
        raise ValueError("Invalid contact number")

    consumer = Consumer(consumer_name=consumer_name, consumer_address=consumer_address, contact_number=contact_number)
    db_session.add(consumer)
    db_session.commit()
    return consumer

def update_consumer(consumer_id, consumer_name, consumer_address, contact_number):
    consumer = get_consumer_by_id(consumer_id)
    if consumer:
        consumer.consumer_name = consumer_name
        consumer.consumer_address = consumer_address
        consumer.contact_number = contact_number
        db_session.commit()
    return consumer

def delete_consumer(consumer_id):
    consumer = get_consumer_by_id(consumer_id)
    if consumer:
        db_session.delete(consumer)
        db_session.commit()
    return consumer

# DAO functions for Product
def get_product_by_id(product_id):
    return db_session.query(Product).filter(Product.product_id == product_id).first()

def get_all_products():
    return db_session.query(Product).all()

def create_product(product_name, amount, description):
    # Validate product_name using a regular expression
    if not re.match(r'^[A-Za-z0-9\s]+$', product_name):
        raise ValueError("Invalid product name")

    product = Product(product_name=product_name, amount=amount, description=description)
    db_session.add(product)
    db_session.commit()
    return product

def update_product(product_id, product_name, amount, description):
    product = get_product_by_id(product_id)
    if product:
        product.product_name = product_name
        product.amount = amount
        product.description = description
        db_session.commit()
    return product

def delete_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        db_session.delete(product)
        db_session.commit()
    return product

# DAO functions for SupplierOrder
def get_supplier_order_by_id(order_id):
    print(db_session.query(SupplierOrder).filter(SupplierOrder.order_id == order_id).first())
    return db_session.query(SupplierOrder).filter(SupplierOrder.order_id == order_id).first()

def get_all_supplier_orders():
    return db_session.query(SupplierOrder).all()

def create_supplier_order(supplier_id, stock_id, order_date, quantity):
    product = get_product_by_id(stock_id)
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
    db_session.add(supplier_order)
    db_session.commit()
    return supplier_order

def update_supplier_order(order_id, supplier_id, stock_id, order_date, quantity):
    supplier_order = get_supplier_order_by_id(order_id)
    if supplier_order:
        supplier_order.supplier_id = supplier_id
        supplier_order.stock_id = stock_id
        supplier_order.order_date = order_date
        supplier_order.quantity = quantity
        supplier_order.calculate_total_price()
        db_session.commit()
    return supplier_order

def delete_supplier_order(order_id):
    supplier_order = get_supplier_order_by_id(order_id)
    if supplier_order:
        db_session.delete(supplier_order)
        db_session.commit()
    return supplier_order

# DAO functions for ConsumerOrder
def get_consumer_order_by_id(order_id):
    return db_session.query(ConsumerOrder).filter(ConsumerOrder.order_id == order_id).first()

def get_all_consumer_orders():
    return db_session.query(ConsumerOrder).all()

def create_consumer_order(consumer_id, product_id, order_date, quantity):
    product = get_product_by_id(product_id)
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
    db_session.add(consumer_order)
    db_session.commit()
    return consumer_order

def update_consumer_order(order_id, consumer_id, product_id, order_date, quantity):
    consumer_order = get_consumer_order_by_id(order_id)
    if consumer_order:
        consumer_order.consumer_id = consumer_id
        consumer_order.product_id = product_id
        consumer_order.order_date = order_date
        consumer_order.quantity = quantity
        consumer_order.calculate_total_price()
        db_session.commit()
    return consumer_order

def delete_consumer_order(order_id):
    consumer_order = get_consumer_order_by_id(order_id)
    if consumer_order:
        db_session.delete(consumer_order)
        db_session.commit()
    return consumer_order

# DAO functions for SupplierTransaction
def get_supplier_transaction_by_id(transaction_id):
    return db_session.query(SupplierTransaction).filter(SupplierTransaction.transaction_id == transaction_id).first()

def get_all_supplier_transactions():
    return db_session.query(SupplierTransaction).all()

def create_supplier_transaction(order_id, supplier_id,  transaction_date):
    supplier = get_supplier_by_id(supplier_id)
    order = get_supplier_order_by_id(order_id)
    if supplier and order:
        supplier_transaction = SupplierTransaction(
            supplier_id=supplier_id,
            order_id=order_id,
            transaction_date=transaction_date
        )
        supplier_transaction.amount = order.total_amount

        db_session.add(supplier_transaction)
        db_session.commit()
        return supplier_transaction
    else:
        return None


def update_supplier_transaction(transaction_id, supplier_id, order_id, transaction_date):
    supplier_transaction = get_supplier_transaction_by_id(transaction_id)
    if supplier_transaction:
        supplier_transaction.supplier_id = supplier_id
        supplier_transaction.order_id = order_id
        supplier_transaction.transaction_date = transaction_date
        supplier_transaction.set_amount_from_order()  

        db_session.commit()
    return supplier_transaction



def delete_supplier_transaction(transaction_id):
    supplier_transaction = get_supplier_transaction_by_id(transaction_id)
    if supplier_transaction:
        db_session.delete(supplier_transaction)
        db_session.commit()
    return supplier_transaction

# DAO functions for ConsumerTransaction
def get_consumer_transaction_by_id(transaction_id):
    return db_session.query(ConsumerTransaction).filter(ConsumerTransaction.transaction_id == transaction_id).first()

def get_all_consumer_transactions():
    return db_session.query(ConsumerTransaction).all()

def create_consumer_transaction(consumer_id, order_id, stock_id, transaction_date):
    consumer = get_consumer_by_id(consumer_id)
    order = get_consumer_order_by_id(order_id)
    stock = get_stock_by_id(stock_id)
    if consumer and order and stock:
        total_amount = order.total_amount  
        transaction = ConsumerTransaction(
            consumer_id=consumer_id,
            order_id=order_id,
            stock_id=stock_id,
            transaction_date=transaction_date,
            amount=total_amount  
        )
        db_session.add(transaction)
        db_session.commit()
        return transaction
    else:
        return None




def update_consumer_transaction(transaction_id, amount=None, transaction_date=None):
    transaction = get_consumer_transaction_by_id(transaction_id)
    if transaction:
        if amount is not None:
            transaction.amount = amount
        if transaction_date:
            transaction.transaction_date = transaction_date
        db_session.commit()
    return transaction

def delete_consumer_transaction(transaction_id):
    consumer_transaction = get_consumer_transaction_by_id(transaction_id)
    if consumer_transaction:
        db_session.delete(consumer_transaction)
        db_session.commit()
    return consumer_transaction
