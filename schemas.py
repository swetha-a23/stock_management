from typing import List, Optional, Dict, Any
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
    def __init__(
        self,
        product_id: int,
        product_name: str,
        amount: float,
        description: str
    ):
        self.product_id = product_id
        self.product_name = product_name
        self.amount = amount
        self.description = description


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
        supplier_daos = SupplierDAO.get_all_suppliers()
        supplier_schemas = []
        for supplier_dao in supplier_daos:
            supplier_schema = {}
            supplier_schema["supplier_id"] = supplier_dao.supplier_id
            supplier_schema["supplier_name"] = supplier_dao.supplier_name
            supplier_schema["supplier_address"] = supplier_dao.supplier_address
            supplier_schema["contact_number"] = supplier_dao.contact_number
            supplier_schemas.append(supplier_schema)
        return supplier_schemas


        

    
    def get_supplier_by_id(self, supplier_id: int) -> SupplierSchema:
        supplier_dao = SupplierDAO.get_supplier_by_id(supplier_id)
        supplier_schema = {
            "supplier_id": supplier_dao.supplier_id,
            "supplier_name": supplier_dao.supplier_name,
            "supplier_address": supplier_dao.supplier_address,
            "contact_number": supplier_dao.contact_number
        }
        return supplier_schema

    
    def get_all_stock(self) -> List[StockSchema]:
        stock_daos = StockDAO.get_all_stock()
        stock_schemas = []
        for stock_dao in stock_daos:
            stock_schema = {}
            stock_schema["stock_id"] = stock_dao.stock_id
            stock_schema["product_id"] = stock_dao.product_id
            stock_schema["quantity"] = stock_dao.quantity
            stock_schema["location"] = stock_dao.location
            stock_schemas.append(stock_schema)
        return stock_schemas

        

    
    def get_stock_by_id(self, stock_id: int) -> StockSchema:
        StockDao = StockDAO.get_stock_by_id(stock_id)
        StockSchema = {}
        StockSchema["stock_id"]=StockDao.stock_id
        StockSchema["product_id"]=StockDao.product_id
        StockSchema["quantity"]=StockDao.quantity
        StockSchema["location"]=StockDao.location
        return StockSchema
        
        

    
    def get_all_consumers(self) -> List[ConsumerSchema]:
        ConsumerDao = ConsumerDAO.get_all_consumers()
        ConsumerSchema = {}
        ConsumerSchema["consumer_id"]=ConsumerDao.consumer_id
        ConsumerSchema["consumer_name"]=ConsumerDao.consumer_name
        ConsumerSchema["consumer_address"]=ConsumerDao.consumer_address
        ConsumerSchema["consumer_number"]=ConsumerDao.consumer_number
        return ConsumerSchema

    
    def get_consumer_by_id(self, consumer_id: int) -> ConsumerSchema:
        ConsumerDao = ConsumerDAO.get_consumer_by_id(consumer_id)
        ConsumerSchema = {}
        ConsumerSchema["consumer_id"]=ConsumerDao.consumer_id
        ConsumerSchema["consumer_name"]=ConsumerDao.consumer_name
        ConsumerSchema["consumer_address"]=ConsumerDao.consumer_address
        ConsumerSchema["consumer_number"]=ConsumerDao.consumer_number
        return ConsumerSchema
        
        

    
    def get_all_products(self) -> List[ProductSchema]:
        product_daos = ProductDAO.get_all_products()
        product_schemas = []
        for product_dao in product_daos:
            product_schema = {}
            product_schema["product_id"] = product_dao.product_id
            product_schema["product_name"] = product_dao.product_name
            product_schema["amount"] = product_dao.amount
            product_schema["description"] = product_dao.description
            product_schemas.append(product_schema)
        return product_schemas


    def get_product_by_id(self, product_id: int) -> Optional[Dict[str, Any]]:
        product_dao = ProductDAO.get_product_by_id(product_id)
        if product_dao:
            product_dict = {
                "product_id": product_dao.product_id,
                "product_name": product_dao.product_name,
                "amount": product_dao.amount,
                "description": product_dao.description
            }
            return product_dict
        return None


    def get_all_supplier_orders(self) -> List[SupplierOrderSchema]:
        supplier_order_daos = SupplierOrderDAO.get_all_supplier_orders()
        supplier_order_schemas = []
        for supplier_order_dao in supplier_order_daos:
            supplier_order_schema = SupplierOrderSchema(
                order_id=supplier_order_dao.order_id,
                supplier_id=supplier_order_dao.supplier_id,
                stock_id=supplier_order_dao.stock_id,
                Order_date=supplier_order_dao.Order_date,
                quantity=supplier_order_dao.quantity,
                total_amount=supplier_order_dao.total_amount
            )
            supplier_order_schemas.append(supplier_order_schema)
        return supplier_order_schemas

    def get_supplier_order_by_id(self, order_id: int) -> Optional[SupplierOrderSchema]:
        supplier_order_dao = SupplierOrderDAO.get_supplier_order_by_id(order_id)
        if supplier_order_dao:
            supplier_order_schema = SupplierOrderSchema(
                order_id=supplier_order_dao.order_id,
                supplier_id=supplier_order_dao.supplier_id,
                stock_id=supplier_order_dao.stock_id,
                Order_date=supplier_order_dao.Order_date,
                quantity=supplier_order_dao.quantity,
                total_amount=supplier_order_dao.total_amount
            )
            return supplier_order_schema
        return None

    def get_all_consumer_orders(self) -> List[ConsumerOrderSchema]:
        consumer_order_daos = ConsumerOrderDAO.get_all_consumer_orders()
        consumer_order_schemas = []
        for consumer_order_dao in consumer_order_daos:
            consumer_order_schema = ConsumerOrderSchema(
                order_id=consumer_order_dao.order_id,
                consumer_id=consumer_order_dao.consumer_id,
                product_id=consumer_order_dao.product_id,
                Order_date=consumer_order_dao.Order_date,
                quantity=consumer_order_dao.quantity,
                total_amount=consumer_order_dao.total_amount
            )
            consumer_order_schemas.append(consumer_order_schema)
        return consumer_order_schemas

    def get_consumer_order_by_id(self, order_id: int) -> Optional[ConsumerOrderSchema]:
        consumer_order_dao = ConsumerOrderDAO.get_consumer_order_by_id(order_id)
        if consumer_order_dao:
            consumer_order_schema = ConsumerOrderSchema(
                order_id=consumer_order_dao.order_id,
                consumer_id=consumer_order_dao.consumer_id,
                product_id=consumer_order_dao.product_id,
                Order_date=consumer_order_dao.Order_date,
                quantity=consumer_order_dao.quantity,
                total_amount=consumer_order_dao.total_amount
            )
            return consumer_order_schema
        return None

    def get_all_supplier_transactions(self) -> List[SupplierTransactionSchema]:
        supplier_transaction_daos = SupplierTransactionDAO.get_all_supplier_transactions()
        supplier_transaction_schemas = []
        for supplier_transaction_dao in supplier_transaction_daos:
            supplier_transaction_schema = SupplierTransactionSchema(
                transaction_id=supplier_transaction_dao.transaction_id,
                supplier_id=supplier_transaction_dao.supplier_id,
                Order_id=supplier_transaction_dao.Order_id,
                amount=supplier_transaction_dao.amount,
                transaction_date=supplier_transaction_dao.transaction_date
            )
            supplier_transaction_schemas.append(supplier_transaction_schema)
        return supplier_transaction_schemas

    def get_supplier_transaction_by_id(self, transaction_id: int) -> Optional[SupplierTransactionSchema]:
        supplier_transaction_dao = SupplierTransactionDAO.get_supplier_transaction_by_id(transaction_id)
        if supplier_transaction_dao:
            supplier_transaction_schema = SupplierTransactionSchema(
                transaction_id=supplier_transaction_dao.transaction_id,
                supplier_id=supplier_transaction_dao.supplier_id,
                Order_id=supplier_transaction_dao.Order_id,
                amount=supplier_transaction_dao.amount,
                transaction_date=supplier_transaction_dao.transaction_date
            )
            return supplier_transaction_schema
        return None

    def get_all_consumer_transactions(self) -> List[ConsumerTransactionSchema]:
        consumer_transaction_daos = ConsumerTransactionDAO.get_all_consumer_transactions()
        consumer_transaction_schemas = []
        for consumer_transaction_dao in consumer_transaction_daos:
            consumer_transaction_schema = ConsumerTransactionSchema(
                transaction_id=consumer_transaction_dao.transaction_id,
                consumer_id=consumer_transaction_dao.consumer_id,
                stock_id=consumer_transaction_dao.stock_id,
                order_id=consumer_transaction_dao.order_id,
                transaction_date=consumer_transaction_dao.transaction_date,
                amount=consumer_transaction_dao.amount
            )
            consumer_transaction_schemas.append(consumer_transaction_schema)
        return consumer_transaction_schemas

    def get_consumer_transaction_by_id(self, transaction_id: int) -> Optional[ConsumerTransactionSchema]:
        consumer_transaction_dao = ConsumerTransactionDAO.get_consumer_transaction_by_id(transaction_id)
        if consumer_transaction_dao:
            consumer_transaction_schema = ConsumerTransactionSchema(
                transaction_id=consumer_transaction_dao.transaction_id,
                consumer_id=consumer_transaction_dao.consumer_id,
                stock_id=consumer_transaction_dao.stock_id,
                order_id=consumer_transaction_dao.order_id,
                transaction_date=consumer_transaction_dao.transaction_date,
                amount=consumer_transaction_dao.amount
            )
            return consumer_transaction_schema
        return None



class Mutation:

    def create_supplier(
        supplier_name: str,
        supplier_address: str,
        contact_number: str
    ) -> SupplierSchema:
        SupplierDao = SupplierDAO.create_supplier(supplier_name, supplier_address, contact_number)
        SupplierSchema = SupplierSchema(
            supplier_id=SupplierDao.supplier_id,
            supplier_name=SupplierDao.supplier_name,
            supplier_address=SupplierDao.supplier_address,
            contact_number=SupplierDao.contact_number
        )
        return SupplierSchema


    def update_supplier(
        supplier_id: int,
        supplier_name: str,
        supplier_address: str,
        contact_number: str,
    ) -> SupplierSchema:
        SupplierDao = SupplierDAO.update_supplier(supplier_id, supplier_name, supplier_address, contact_number)
        SupplierSchema = SupplierSchema(
            supplier_id=SupplierDao.supplier_id,
            supplier_name=SupplierDao.supplier_name,
            supplier_address=SupplierDao.supplier_address,
            contact_number=SupplierDao.contact_number
        )
        return SupplierSchema


    def delete_supplier(supplier_id: int) -> SupplierSchema:
        supplier_id = SupplierDAO.delete_supplier(supplier_id)
        return SupplierSchema(supplier_id=supplier_id)


    def create_stock(product_id: int, quantity: int, location: str) -> StockSchema:
        StockDao = StockDAO.create_stock(product_id, quantity, location)
        StockSchema = StockSchema(
            stock_id=StockDao.stock_id,
            product_id=StockDao.product_id,
            quantity=StockDao.quantity,
            location=StockDao.location
        )
        return StockSchema


    def update_stock(stock_id: int, product_id: int, quantity: int, location: str) -> StockSchema:
        StockDao = StockDAO.update_stock(stock_id, product_id, quantity, location)
        StockSchema = StockSchema(
            stock_id=StockDao.stock_id,
            product_id=StockDao.product_id,
            quantity=StockDao.quantity,
            location=StockDao.location
        )
        return StockSchema


    def delete_stock(stock_id: int) -> StockSchema:
        stock_id = StockDAO.delete_stock(stock_id)
        return StockSchema(stock_id=stock_id)


    def create_consumer(
        consumer_name: str,
        consumer_address: str,
        contact_number: str
    ) -> ConsumerSchema:
        ConsumerDao = ConsumerDAO.create_consumer(consumer_name, consumer_address, contact_number)
        ConsumerSchema = ConsumerSchema(
            consumer_id=ConsumerDao.consumer_id,
            consumer_name=ConsumerDao.consumer_name,
            consumer_address=ConsumerDao.consumer_address,
            contact_number=ConsumerDao.contact_number
        )
        return ConsumerSchema


    def update_consumer(
        consumer_id: int,
        consumer_name: str,
        consumer_address: str,
        contact_number: str,
    ) -> ConsumerSchema:
        ConsumerDao = ConsumerDAO.update_consumer(consumer_id, consumer_name, consumer_address, contact_number)
        ConsumerSchema = ConsumerSchema(
            consumer_id=ConsumerDao.consumer_id,
            consumer_name=ConsumerDao.consumer_name,
            consumer_address=ConsumerDao.consumer_address,
            contact_number=ConsumerDao.contact_number
        )
        return ConsumerSchema


    def delete_consumer(consumer_id: int) -> ConsumerSchema:
        consumer_id = ConsumerDAO.delete_consumer(consumer_id)
        return ConsumerSchema(consumer_id=consumer_id)


    def create_product(
        product_name: str,
        amount: float,
        description: str
    ) -> dict:
        ProductDao = ProductDAO.create_product(product_name, amount, description)
        ProductSchema = {
            "product_id": ProductDao.product_id,
            "product_name": ProductDao.product_name,
            "amount": ProductDao.amount,
            "description": ProductDao.description
        }
        return ProductSchema




    def update_product(
        product_id: int,
        product_name: str,
        amount: float,
        description: str
    ) -> dict:
        ProductDao = ProductDAO.update_product(product_id, product_name, amount, description)
        ProductSchema = {
            "product_id": ProductDao.product_id,
            "product_name": ProductDao.product_name,
            "amount": ProductDao.amount,
            "description": ProductDao.description
        }
        return ProductSchema



    def delete_product(product_id: int) -> dict:
        ProductDAO.delete_product(product_id)
        return {"product_id": product_id}



    def create_supplier_order(
        supplier_id: int,
        stock_id: int,
        order_date: datetime,
        quantity: int
    ) -> SupplierOrderSchema:
        SupplierOrderDao = SupplierOrderDAO.create_supplier_order(supplier_id, stock_id, order_date, quantity)
        SupplierOrderSchema = SupplierOrderSchema(
            order_id=SupplierOrderDao.order_id,
            supplier_id=SupplierOrderDao.supplier_id,
            stock_id=SupplierOrderDao.stock_id,
            order_date=SupplierOrderDao.order_date,
            quantity=SupplierOrderDao.quantity
        )
        return SupplierOrderSchema


    def update_supplier_order(
        order_id: int,
        supplier_id: int,
        stock_id: int,
        order_date: datetime,
        quantity: int
    ) -> SupplierOrderSchema:
        SupplierOrderDao = SupplierOrderDAO.update_supplier_order(order_id, supplier_id, stock_id, order_date, quantity)
        SupplierOrderSchema = SupplierOrderSchema(
            order_id=SupplierOrderDao.order_id,
            supplier_id=SupplierOrderDao.supplier_id,
            stock_id=SupplierOrderDao.stock_id,
            order_date=SupplierOrderDao.order_date,
            quantity=SupplierOrderDao.quantity
        )
        return SupplierOrderSchema


    def delete_supplier_order(order_id: int) -> SupplierOrderSchema:
        order_id = SupplierOrderDAO.delete_supplier_order(order_id)
        return SupplierOrderSchema(order_id=order_id)


    def create_consumer_order(
        consumer_id: int,
        product_id: int,
        order_date: datetime,
        quantity: int
    ) -> ConsumerOrderSchema:
        ConsumerOrderDao = ConsumerOrderDAO.create_consumer_order(consumer_id, product_id, order_date, quantity)
        ConsumerOrderSchema = ConsumerOrderSchema(
            order_id=ConsumerOrderDao.order_id,
            consumer_id=ConsumerOrderDao.consumer_id,
            product_id=ConsumerOrderDao.product_id,
            order_date=ConsumerOrderDao.order_date,
            quantity=ConsumerOrderDao.quantity
        )
        return ConsumerOrderSchema


    def update_consumer_order(
        order_id: int,
        consumer_id: int,
        product_id: int,
        order_date: datetime,
        quantity: int
    ) -> ConsumerOrderSchema:
        ConsumerOrderDao = ConsumerOrderDAO.update_consumer_order(order_id, consumer_id, product_id, order_date, quantity)
        ConsumerOrderSchema = ConsumerOrderSchema(
            order_id=ConsumerOrderDao.order_id,
            consumer_id=ConsumerOrderDao.consumer_id,
            product_id=ConsumerOrderDao.product_id,
            order_date=ConsumerOrderDao.order_date,
            quantity=ConsumerOrderDao.quantity
        )
        return ConsumerOrderSchema


    def delete_consumer_order(order_id: int) -> ConsumerOrderSchema:
        order_id = ConsumerOrderDAO.delete_consumer_order(order_id)
        return ConsumerOrderSchema(order_id=order_id)


    def create_supplier_transaction(
        supplier_id: int,
        order_id: int,
        transaction_date: datetime
    ) -> SupplierTransactionSchema:
        SupplierTransactionsDao = SupplierTransactionDAO.create_supplier_transaction(supplier_id, order_id, transaction_date)
        SupplierTransactionsSchema = SupplierTransactionSchema(
            transaction_id=SupplierTransactionsDao.transaction_id,
            supplier_id=SupplierTransactionsDao.supplier_id,
            Order_id=SupplierTransactionsDao.Order_id,
            transaction_date=SupplierTransactionsDao.transaction_date
        )
        return SupplierTransactionsSchema


    def update_supplier_transaction(
        transaction_id: int,
        supplier_id: int,
        order_id: int,
        transaction_date: datetime
    ) -> SupplierTransactionSchema:
        SupplierTransactionsDao = SupplierTransactionDAO.update_supplier_transaction(
            transaction_id, supplier_id, order_id, transaction_date)
        if not SupplierTransactionsDao:
            raise ValueError("Invalid transaction ID")
        SupplierTransactionsSchema = SupplierTransactionSchema(
            transaction_id=SupplierTransactionsDao.transaction_id,
            supplier_id=SupplierTransactionsDao.supplier_id,
            Order_id=SupplierTransactionsDao.Order_id,
            transaction_date=SupplierTransactionsDao.transaction_date
        )
        return SupplierTransactionsSchema


    def delete_supplier_transaction(transaction_id: int) -> SupplierTransactionSchema:
        SupplierTransactionsDao = SupplierTransactionDAO.delete_supplier_transaction(transaction_id)
        if not SupplierTransactionsDao:
            raise ValueError("Invalid transaction ID")
        return SupplierTransactionSchema(transaction_id=SupplierTransactionsDao.transaction_id)


    def create_consumer_transaction(
        consumer_id: int,
        order_id: int,
        stock_id: int,
        transaction_date: datetime
    ) -> ConsumerTransactionSchema:
        ConsumerTransactionsDao = ConsumerTransactionDAO.create_consumer_transaction(
            consumer_id, order_id, stock_id, transaction_date)
        ConsumerTransactionsSchema = ConsumerTransactionSchema(
            transaction_id=ConsumerTransactionsDao.transaction_id,
            consumer_id=ConsumerTransactionsDao.consumer_id,
            stock_id=ConsumerTransactionsDao.stock_id,
            order_id=ConsumerTransactionsDao.order_id,
            transaction_date=ConsumerTransactionsDao.transaction_date
        )
        return ConsumerTransactionsSchema


    def update_consumer_transaction(
        transaction_id: int,
        consumer_id: int,
        order_id: int,
        stock_id: int,
        transaction_date: datetime
    ) -> ConsumerTransactionSchema:
        ConsumerTransactionsDao = ConsumerTransactionDAO.update_consumer_transaction(
            transaction_id, consumer_id, order_id, stock_id, transaction_date)
        if not ConsumerTransactionsDao:
            raise ValueError("Invalid transaction ID")
        ConsumerTransactionsSchema = ConsumerTransactionSchema(
            transaction_id=ConsumerTransactionsDao.transaction_id,
            consumer_id=ConsumerTransactionsDao.consumer_id,
            stock_id=ConsumerTransactionsDao.stock_id,
            order_id=ConsumerTransactionsDao.order_id,
            transaction_date=ConsumerTransactionsDao.transaction_date
        )
        return ConsumerTransactionsSchema


    def delete_consumer_transaction(transaction_id: int) -> ConsumerTransactionSchema:
        ConsumerTransactionsDao = ConsumerTransactionDAO.delete_consumer_transaction(transaction_id)
        if not ConsumerTransactionsDao:
            raise ValueError("Invalid transaction ID")
        return ConsumerTransactionSchema(transaction_id=ConsumerTransactionsDao.transaction_id)

        