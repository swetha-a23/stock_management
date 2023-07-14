from typing import List
from models import *
from datetime import datetime
from dao import *
import json



class SupplierSchema:
    supplier_id: int
    supplier_name: str
    supplier_address: str
    contact_number: str



class StockSchema:
    stock_id: int
    product_id: int
    quantity: int
    location: str


class ConsumerSchema:
    consumer_id: int
    consumer_name: str
    consumer_address: str
    contact_number: str


class ProductSchema:
    product_id: int
    product_name: str
    amount: float
    description: str

class SupplierOrderSchema:
    order_id: int
    supplier_id: int
    stock_id: int
    order_date: datetime
    quantity: int
    total_amount: int
    product: ProductSchema


class ConsumerOrderSchema:
    order_id: int
    consumer_id: int
    product_id: int
    order_date: datetime
    quantity: int
    total_amount: int
    product: ProductSchema



class SupplierTransactionSchema:
    transaction_id: int
    supplier_id: int
    order_id: int
    amount: float
    transaction_date: str
    order: SupplierOrderSchema





class ConsumerTransactionSchema:
    transaction_id: int
    consumer_id: int
    order_id: int
    stock_id: int
    transaction_date: datetime
    amount: float
    order: ConsumerOrderSchema




class Query:
    
    def get_all_suppliers(self) -> List[SupplierSchema]:
        SupplierDao = Supplier.get_all_suppliers()
        SupplierSchema = {}
        SupplierSchema["supplier_id"]=SupplierDao.supplier_id
        SupplierSchema["supplier_name"]=SupplierDao.supplier_name
        SupplierSchema["supplier_address"]=SupplierDao.supplier_address
        SupplierSchema["contact_number"]=SupplierDao.contact_number


        

    
    def get_supplier_by_id(self, supplier_id: int) -> SupplierSchema:
        SupplierDao = Supplier.get_supplier_by_id(supplier_id)
        SupplierSchema = {}
        SupplierSchema["supplier_id"]=SupplierDao.supplier_id
        SupplierSchema["supplier_name"]=SupplierDao.supplier_name
        SupplierSchema["supplier_address"]=SupplierDao.supplier_address
        SupplierSchema["contact_number"]=SupplierDao.contact_number

    
    def get_all_stock(self) -> List[StockSchema]:
        StockDao = Stock.get_all_stock()
        StockSchema = {}
        StockSchema["stock_id"]=StockDao.stock_id
        StockSchema["product_id"]=StockDao.product_id
        StockSchema["quantity"]=StockDao.quantity
        StockSchema["location"]=StockDao.location
        

    
    def get_stock_by_id(self, stock_id: int) -> StockSchema:
        StockDao = Stock.get_stock_by_id(stock_id)
        StockSchema = {}
        StockSchema["stock_id"]=StockDao.stock_id
        StockSchema["product_id"]=StockDao.product_id
        StockSchema["quantity"]=StockDao.quantity
        StockSchema["location"]=StockDao.location
        
        

    
    def get_all_consumers(self) -> List[ConsumerSchema]:
        ConsumerDao = Consumer.get_all_consumers()
        ConsumerSchema = {}
        ConsumerSchema["consumer_id"]=ConsumerDao.consumer_id
        ConsumerSchema["consumer_name"]=ConsumerDao.consumer_name
        ConsumerSchema["consumer_address"]=ConsumerDao.consumer_address
        ConsumerSchema["consumer_number"]=ConsumerDao.consumer_number

    
    def get_consumer_by_id(self, consumer_id: int) -> ConsumerSchema:
        ConsumerDao = Consumer.get_consumer_by_id(consumer_id)
        ConsumerSchema = {}
        ConsumerSchema["consumer_id"]=ConsumerDao.consumer_id
        ConsumerSchema["consumer_name"]=ConsumerDao.consumer_name
        ConsumerSchema["consumer_address"]=ConsumerDao.consumer_address
        ConsumerSchema["consumer_number"]=ConsumerDao.consumer_number
        
        

    
    def get_all_products(self) -> List[ProductSchema]:
        ProductDao = Product.get_all_products()
        ProductSchema = {}
        ProductSchema["product_id"]=ProductDao.product_id
        ProductSchema["product_name"]=ProductDao.product_name
        ProductSchema["amount"] = ProductDao.amount
        ProductSchema["description"] = ProductDao.description
        return Product

    
    def get_product_by_id(self, product_id: int) -> ProductSchema:
        ProductDao = Product.get_product_by_id(product_id)
        ProductSchema = {}
        ProductSchema["product_id"]=ProductDao.product_id
        ProductSchema["product_name"]=ProductDao.name
        ProductSchema["amount"] = ProductDao.amount
        ProductSchema["description"] = ProductDao.description
        return Product

    
    def get_all_supplier_orders(self) -> List[SupplierOrderSchema]:
        SupplierOrderDao = SupplierOrder.get_all_supplier_orders()
        SupplierOrderSchema = {}
        SupplierOrderSchema["order_id"]=SupplierOrderDao.order_id
        SupplierOrderSchema["supplier_id"]=SupplierOrderDao.supplier_id
        SupplierOrderSchema["stock_id"] = SupplierOrderDao.stock_id
        SupplierOrderSchema["Order_date"] = SupplierOrderDao.Order_date
        SupplierOrderSchema["quantity"] = SupplierOrderDao.quantity
        SupplierOrderSchema["total_amount"] = SupplierOrderDao.total_amount
        return SupplierOrder 
        

    
    def get_supplier_order_by_id(self, order_id: int) -> SupplierOrderSchema:
        SupplierOrderDao = SupplierOrder.get_supplier_order_by_id(order_id)
        SupplierOrderSchema = {}
        SupplierOrderSchema["order_id"]=SupplierOrderDao.order_id
        SupplierOrderSchema["supplier_id"]=SupplierOrderDao.supplier_id
        SupplierOrderSchema["stock_id"] = SupplierOrderDao.stock_id
        SupplierOrderSchema["Order_date"] = SupplierOrderDao.Order_date
        SupplierOrderSchema["quantity"] = SupplierOrderDao.quantity
        SupplierOrderSchema["total_amount"] = SupplierOrderDao.total_amount
        return SupplierOrder 

    
    def get_all_consumer_orders(self) -> List[ConsumerOrderSchema]:
        ConsumerOrderDao = ConsumerOrder.get_all_consumer_orders()
        ConsumerOrderSchema = {}
        ConsumerOrderSchema["order_id"]=ConsumerOrderDao.order_id
        ConsumerOrderSchema["consumer_id"]=ConsumerOrderDao.consumer_id
        ConsumerOrderSchema["product_id"] = ConsumerOrderDao.product_id
        ConsumerOrderSchema["Order_date"] = ConsumerOrderDao.Order_date
        ConsumerOrderSchema["quantity"] = ConsumerOrderDao.quantity
        ConsumerOrderSchema["total_amount"] = ConsumerOrderDao.total_amount
        return ConsumerOrder
        

    
    def get_consumer_order_by_id(self, order_id: int) -> ConsumerOrderSchema:
        ConsumerOrderDao = ConsumerOrder.get_consumer_order_by_id(order_id)
        ConsumerOrderSchema = {}
        ConsumerOrderSchema["order_id"]=ConsumerOrderDao.order_id
        ConsumerOrderSchema["consumer_id"]=ConsumerOrderDao.supplier_id
        ConsumerOrderSchema["product_id"] = ConsumerOrderDao.product_id
        ConsumerOrderSchema["Order_date"] = ConsumerOrderDao.Order_date
        ConsumerOrderSchema["quantity"] = ConsumerOrderDao.quantity
        ConsumerOrderSchema["total_amount"] = ConsumerOrderDao.total_amount
        return ConsumerOrder
        

    
    def get_all_supplier_transactions(self) -> List[SupplierTransactionSchema]:
        SupplierTransactionsDao = SupplierTransaction.get_all_supplier_transactions()
        SupplierTransactionsSchema = {}
        SupplierTransactionsSchema["transaction_id"]=SupplierTransactionsDao.order_id
        SupplierTransactionsSchema["supplier_id"]=SupplierTransactionsDao.supplier_id
        SupplierTransactionsSchema["Order_id"] = SupplierTransactionsDao.Order_id
        SupplierTransactionsSchema["amount"] = SupplierTransactionsDao.amount
        SupplierTransactionsSchema["transaction_date"] = SupplierTransactionsDao.transaction_date
        return SupplierTransaction
        

    
    def get_supplier_transaction_by_id(self, transaction_id : int) -> SupplierTransactionSchema:
        SupplierTransactionsDao = SupplierTransaction.get_supplier_transaction_by_id(transaction_id)
        SupplierTransactionsSchema = {}
        SupplierTransactionsSchema["transaction_id"]=SupplierTransactionsDao.transaction_id
        SupplierTransactionsSchema["supplier_id"]=SupplierTransactionsDao.supplier_id
        SupplierTransactionsSchema["Order_id"] = SupplierTransactionsDao.Order_id
        SupplierTransactionsSchema["amount"] = SupplierTransactionsDao.amount
        SupplierTransactionsSchema["transaction_date"] = SupplierTransactionsDao.transaction_date
        return SupplierTransaction
        
        

   
    def get_all_consumer_transactions(self) -> List[ConsumerTransactionSchema]:
        ConsumerTransactionsDao = ConsumerTransaction.get_all_consumer_transactions()
        ConsumerTransactionsSchema = {}
        ConsumerTransactionsSchema["transaction_id"]=ConsumerTransactionsDao.transaction_id
        ConsumerTransactionsSchema["consumer_id"]=ConsumerTransactionsDao.consumer_id
        ConsumerTransactionsSchema["stock_id"] = ConsumerTransactionsDao.stock_id
        ConsumerTransactionsSchema["order_id"] = ConsumerTransactionsDao.order_id
        ConsumerTransactionsSchema["transaction_date"] = ConsumerTransactionsDao.transaction_date
        ConsumerTransactionsSchema["amount"] = ConsumerTransactionsDao.amount
        return ConsumerTransaction
        

   
    def get_consumer_transaction_by_id(self, transaction_id: int) -> ConsumerTransactionSchema:
        ConsumerTransactionsDao = ConsumerTransaction.get_consumer_transaction_by_id(transaction_id)
        ConsumerTransactionsSchema = {}
        ConsumerTransactionsSchema["transaction_id"]= ConsumerTransactionsDao.order_id
        ConsumerTransactionsSchema["consumer_id"]= ConsumerTransactionsDao.supplier_id
        ConsumerTransactionsSchema["stock_id"] =  ConsumerTransactionsDao.Order_id
        ConsumerTransactionsSchema["order_id"] =  ConsumerTransactionsDao.order_id
        ConsumerTransactionsSchema["transaction_date"] =  ConsumerTransactionsDao.transaction_date
        ConsumerTransactionsSchema["amount"] =  ConsumerTransactionsDao.amount
        return ConsumerTransaction 


class Mutation:
    
    def create_supplier(supplier_name: str, supplier_address: str, contact_number: str) -> SupplierSchema:
        SupplierDao =Supplier.create_supplier(supplier_name,supplier_address,contact_number)
        SupplierSchema={}
        SupplierSchema["supplier_name"]=SupplierDao.supplier_name
        SupplierSchema["supplier_address"]=SupplierDao.supplier_address
        SupplierSchema["contact_number"]=SupplierDao.contact_number
        return Supplier

    
    def update_supplier(
        supplier_id: int,
        supplier_name: str,
        supplier_address: str,
        contact_number: str,
    ) -> SupplierSchema:
        SupplierDao =Supplier.update_supplier(supplier_name,supplier_address,contact_number)
        SupplierSchema={}
        SupplierSchema["supplier_id"]=SupplierDao.supplier_id
        SupplierSchema["supplier_name"]=SupplierDao.supplier_name
        SupplierSchema["supplier_address"]=SupplierDao.supplier_address
        SupplierSchema["contact_number"]=SupplierDao.contact_number
        return Supplier
        
        

    
    def delete_supplier(supplier_id: int) -> SupplierSchema:
        supplier_id=Supplier.delete_supplier(supplier_id)
        return {"supplier_id":supplier_id}


    
        

    
    def create_stock(self,product_id: int, quantity: int, location: str) -> StockSchema:
        StockDao = Stock.create_stock(product_id,quantity,location)
        StockSchema={}
        StockSchema["product_id"]=StockDao.product_id
        StockSchema["quantity"]=StockDao.quantity
        StockSchema["location"]=StockDao.location
        return Stock
        

   
    def update_stock(self,stock_id: int, product_id: int, quantity: int, location: str) -> StockSchema:
        StockDao = Stock.update_stock(stock_id,product_id,quantity,location)
        StockSchema={}
        StockSchema["stock_id"]=StockDao.stock_id
        StockSchema["product_id"]=StockDao.product_id
        StockSchema["quantity"]=StockDao.quantity
        StockSchema["location"]=StockDao.location
        return Stock
        
        

    
    def delete_stock(self, info, stock_id: int) -> StockSchema:
        stock_id=Stock.delete_stock(stock_id)
        return {"stock_id":stock_id}

   
    def create_consumer(self,consumer_name: str, consumer_address: str, contact_number: str) -> ConsumerSchema:
        ConsumerDao = Consumer.create_consumer(consumer_name,consumer_address, contact_number)
        ConsumerSchema = {}
        ConsumerSchema["consumer_name"] = ConsumerDao.consumer_name
        ConsumerSchema["consumer_address"] = ConsumerDao.consumer_address
        ConsumerSchema["contact_number"] = ConsumerDao.contact_number
        return Consumer

    
    def update_consumer(
        self,
        consumer_id: int,
        consumer_name: str,
        consumer_address: str,
        contact_number: str,
    ) -> ConsumerSchema:
        ConsumerDao = Consumer.update_consumer(consumer_id, consumer_name,consumer_address, contact_number)
        ConsumerSchema = {}
        ConsumerSchema["consumer_id"] = ConsumerDao.consumer_id
        ConsumerSchema["consumer_name"] = ConsumerDao.name
        ConsumerSchema["consumer_address"] = ConsumerDao.consumer_address
        ConsumerSchema["contact_number"] = ConsumerDao.contact_number
        return Consumer

        

    
    def delete_consumer(self, info, consumer_id: int) -> ConsumerSchema:
        consumer_id = Consumer.delete_consumer(consumer_id)
        return {"consumer_id": consumer_id}

    
    def create_product(product_name: str, amount: float, description: str) -> ProductSchema:
        ProductDao = Product.create_product(product_name,amount,description)
        ProductSchema={}
        ProductSchema["product_name"]=ProductDao.product_name
        ProductSchema["amount"]=ProductDao.amount
        ProductSchema["description"]=ProductDao.description

    
    def update_product(product_id: int, product_name: str, amount: float, description: str) -> ProductSchema:
        ProductDao = Product.update_product(product_name,amount,description)
        ProductSchema={}
        ProductSchema["product_name"]=ProductDao.product_name
        ProductSchema["amount"]=ProductDao.amount
        ProductSchema["description"]=ProductDao.description
        return Product
        

    
    def delete_product(self, info, product_id: int) -> ProductSchema:
        product_id=Product.delete_product(product_id)
        return {"product_id":product_id}

   
    def create_supplier_order(
        self,
        supplier_id: int,
        stock_id: int,
        order_date: datetime,
        quantity: int,
    ) -> SupplierOrderSchema:
        SupplierOrderDao=SupplierOrder.create_supplier_order(supplier_id,stock_id,order_date,quantity)
        SupplierOrderSchema={}
        SupplierOrderSchema["supplier_id"]=SupplierOrderDao.supplier_id
        SupplierOrderSchema["stock_id"]=SupplierOrderDao.stock_id
        SupplierOrderSchema["order_date"]=SupplierOrderDao.order_date
        SupplierOrderSchema["quantity"]=SupplierOrderDao.quantity

    
    def update_supplier_order(
        self,
        order_id: int,
        supplier_id: int,
        stock_id: int,
        order_date: datetime,
        quantity: int,
    ) -> SupplierOrderSchema:
        SupplierOrderDao=SupplierOrder.update_supplier_order(order_id,supplier_id,stock_id,order_date,quantity)
        SupplierOrderSchema={}
        SupplierOrderSchema["order_id"]=SupplierOrderDao.order_id
        SupplierOrderSchema["supplier_id"]=SupplierOrderDao.supplier_id
        SupplierOrderSchema["stock_id"]=SupplierOrderDao.stock_id
        SupplierOrderSchema["order_date"]=SupplierOrderDao.order_date
        SupplierOrderSchema["quantity"]=SupplierOrderDao.quantity

    
    def delete_supplier_order(self,order_id: int) -> SupplierOrderSchema:
        order_id=SupplierOrder.delete_supplier_order(order_id)
        return{"order_id":order_id}

    
    def create_consumer_order(
        self,
        info,
        consumer_id: int,
        product_id: int,
        order_date: datetime,
        quantity: int,
    ) -> ConsumerOrderSchema:
        ConsumerOrderDao=ConsumerOrder.create_consumer_order(consumer_id,product_id,order_date,quantity)
        ConsumerOrderSchema={}
        ConsumerOrderSchema["consumer_id"]=ConsumerOrderDao.consumer_id
        ConsumerOrderSchema["product_id"]=ConsumerOrderDao.product_id
        ConsumerOrderSchema["order_date"]=ConsumerOrderDao.order_date
        ConsumerOrderSchema["quantity"]=ConsumerOrderDao.quantity
        return ConsumerOrderSchema

    
    def update_consumer_order(
        self,
        order_id: int,
        consumer_id: int,
        product_id: int,
        order_date: datetime,
        quantity: int,
    ) -> ConsumerOrderSchema:
        ConsumerOrderDao=ConsumerOrder.update_consumer_order(order_id,consumer_id,product_id,order_date,quantity)
        ConsumerOrderSchema={}
        ConsumerOrderSchema["order_id"]=ConsumerOrderDao.order_id
        ConsumerOrderSchema["consumer_id"]=ConsumerOrderDao.consumer_id
        ConsumerOrderSchema["product_id"]=ConsumerOrderDao.product_id
        ConsumerOrderSchema["order_date"]=ConsumerOrderDao.order_date
        ConsumerOrderSchema["quantity"]=ConsumerOrderDao.quantity
        return ConsumerOrderSchema

    
    def delete_consumer_order(self, info, order_id: int) -> ConsumerOrderSchema:
        order_id = ConsumerOrder.delete_consumer_order(order_id)
        return {"order_id": order_id}

    
    def create_supplier_transaction(
        self,
        supplier_id: int,
        order_id: int,
        transaction_date: datetime,
    ) -> SupplierTransactionSchema:
        supplier = Supplier.get_supplier_by_id(supplier_id)
        order = SupplierOrder.get_supplier_order_by_id(order_id)
        if supplier and order:
            transaction = SupplierTransaction.create_supplier_transaction(
                supplier_id, order_id, transaction_date)
            SupplierTransactionSchema = {}
            SupplierTransactionSchema["supplier_id"] = transaction.supplier_id
            SupplierTransactionSchema["order_id"] = transaction.order_id
            SupplierTransactionSchema["transaction_date"] = transaction.transaction_date
            return SupplierTransaction
        else:
            raise ValueError("Invalid supplier ID or order ID")

    
    def update_supplier_transaction(
        self,
        transaction_id: int,
        supplier_id: int,
        order_id: int,
        transaction_date: datetime,
    ) -> SupplierTransactionSchema:
        transaction = SupplierTransaction.update_supplier_transaction(
            transaction_id,supplier_id,order_id,transaction_date)
        if not transaction:
            raise ValueError("Invalid transaction ID")
        SupplierTransactionSchema = {}
        SupplierTransactionSchema["transaction_id"] = transaction.transaction_id
        SupplierTransactionSchema["supplier_id"] = transaction.supplier_id
        SupplierTransactionSchema["order_id"] = transaction.order_id
        SupplierTransactionSchema["transaction_date"] = transaction.transaction_date
        return SupplierTransaction
        

    
    def delete_supplier_transaction(self, transaction_id: int) -> SupplierTransactionSchema:
        transaction = SupplierTransaction.delete_supplier_transaction(transaction_id)
        if not transaction:
            raise ValueError("Invalid transaction ID")
        return {"transaction_id": transaction.transaction_id}
        

    
    def create_consumer_transaction(
        self,
        consumer_id: int,
        order_id: int,
        stock_id: int,
        transaction_date: datetime,
    ) -> ConsumerTransactionSchema:
        consumer = Consumer.get_consumer_by_id(consumer_id)
        order = ConsumerOrder.get_consumer_order_by_id(order_id)
        if consumer and order:
            transaction = ConsumerTransaction.create_consumer_transaction(
                consumer_id, order_id,stock_id,transaction_date)
            ConsumerTransactionSchema = {}
            ConsumerTransactionSchema["consumer_id"] = transaction.consumer_id
            ConsumerTransactionSchema["order_id"] = transaction.order_id
            ConsumerTransactionSchema["stock_id"]=transaction.stock_id
            ConsumerTransactionSchema["transaction_date"] = transaction.transaction_date
            return ConsumerTransaction
        else:
            raise ValueError("Invalid consumer ID or order ID")

    
    def update_consumer_transaction(
        self,
        info,
        transaction_id: int,
        consumer_id: int,
        order_id: int,
        stock_id: int,
        transaction_date: datetime,
    ) -> ConsumerTransactionSchema:
        transaction = ConsumerTransaction.update_consumer_transaction(
            transaction_id,consumer_id,order_id,stock_id,transaction_date)
        if not transaction:
            raise ValueError("Invalid transaction ID")
        ConsumerTransactionSchema = {}
        ConsumerTransactionSchema["transaction_id"] = transaction.transaction_id
        ConsumerTransactionSchema["consumer_id"]= transaction.consumer_id
        ConsumerTransactionSchema["order_id"]=transaction.order_id
        ConsumerTransactionSchema["stock_id"]=transaction.stock_id
        ConsumerTransactionSchema["transaction_date"] = transaction.transaction_date
        return ConsumerTransaction

    
    def delete_consumer_transaction(self,transaction_id: int) -> ConsumerTransactionSchema:
        transaction = ConsumerTransaction.delete_consumer_transaction(transaction_id)
        if not transaction:
            raise ValueError("Invalid transaction ID")
        return {"transaction_id": transaction.transaction_id}
        