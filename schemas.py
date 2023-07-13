import strawberry
from typing import List
from datetime import datetime
from resolvers import *
from dao import *

# Supplier Schema
@strawberry.type
class SupplierSchema:
    supplier_id: int
    supplier_name: str
    supplier_address: str
    contact_number: str


# Stock Schema
@strawberry.type
class StockSchema:
    stock_id: int
    product_id: int
    quantity: int
    location: str

# Consumer Schema
@strawberry.type
class ConsumerSchema:
    consumer_id: int
    consumer_name: str
    consumer_address: str
    contact_number: str

# Product Schema
@strawberry.type
class ProductSchema:
    product_id: int
    product_name: str
    amount: float
    description: str

#SupplierOrder
@strawberry.type
class SupplierOrderSchema:
    order_id: int
    supplier_id: int
    stock_id: int
    order_date: datetime
    quantity: int
    total_amount: int
    product: ProductSchema

    @strawberry.field
    def calculate_total_price(self) -> int:
        product = get_product_by_id(self.stock_id)
        if product:
            return self.quantity * product.amount
        return 0

#ConsumerOrder
@strawberry.type
class ConsumerOrderSchema:
    order_id: int
    consumer_id: int
    product_id: int
    order_date: datetime
    quantity: int
    total_amount: int
    product: ProductSchema

    @strawberry.field
    def calculate_total_price(self) -> int:
        product = get_product_by_id(self.product_id)
        if product:
            return self.quantity * product.amount
        return 0


# SupplierTransaction Schema
@strawberry.type
class SupplierTransactionSchema:
    transaction_id: int
    supplier_id: int
    order_id: int
    amount: float
    transaction_date: str
    order: SupplierOrderSchema




# ConsumerTransaction Schema
@strawberry.type
class ConsumerTransactionSchema:
    transaction_id: int
    consumer_id: int
    order_id: int
    stock_id: int
    transaction_date: datetime
    amount: float
    order: ConsumerOrderSchema



# Query Schema
@strawberry.type
class Query:
    @strawberry.field
    def getAllSuppliers(self) -> List[SupplierSchema]:
        return get_all_suppliers()

    @strawberry.field
    def getSupplierById(self, supplier_id: int) -> SupplierSchema:
        return get_supplier_by_id(supplier_id)

    @strawberry.field
    def getAllStocks(self) -> List[StockSchema]:
        return get_all_stock()

    @strawberry.field
    def getStockById(self, stock_id: int) -> StockSchema:
        return get_stock_by_id(stock_id)

    @strawberry.field
    def getAllConsumers(self) -> List[ConsumerSchema]:
        return get_all_consumers()

    @strawberry.field
    def getConsumerById(self, consumer_id: int) -> ConsumerSchema:
        return get_consumer_by_id(consumer_id)

    @strawberry.field
    def getAllProducts(self) -> List[ProductSchema]:
        return get_all_products()

    @strawberry.field
    def getProductById(self, product_id: int) -> ProductSchema:
        return get_product_by_id(product_id)

    @strawberry.field
    def getAllSupplierOrders(self) -> List[SupplierOrderSchema]:
        return get_all_supplier_orders()

    @strawberry.field
    def getSupplierOrderById(self, order_id: int) -> SupplierOrderSchema:
        return get_supplier_order_by_id(order_id)

    @strawberry.field
    def getAllConsumerOrders(self) -> List[ConsumerOrderSchema]:
        return get_all_consumer_orders()

    @strawberry.field
    def getConsumerOrderById(self, order_id: int) -> ConsumerOrderSchema:
        return get_consumer_order_by_id(order_id)

    @strawberry.field
    def getAllSupplierTransactions(self) -> List[SupplierTransactionSchema]:
        return get_all_supplier_transactions()

    @strawberry.field
    def getSupplierTransactionById(self, transaction_id : int) -> SupplierTransactionSchema:
        return get_supplier_transaction_by_id(transaction_id)

    @strawberry.field
    def getAllConsumerTransactions(self) -> List[ConsumerTransactionSchema]:
        return get_all_consumer_transactions()

    @strawberry.field
    def getConsumerTransactionById(self, transaction_id: int) -> ConsumerTransactionSchema:
        return get_consumer_transaction_by_id(transaction_id)


# Mutation Schema
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_supplier(self, info, supplier_name: str, supplier_address: str, contact_number: str) -> SupplierSchema:
        return create_supplier(supplier_name, supplier_address, contact_number)

    @strawberry.mutation
    def update_supplier(
        self,
        info,
        supplier_id: int,
        supplier_name: str,
        supplier_address: str,
        contact_number: str,
    ) -> SupplierSchema:
        return update_supplier(supplier_id, supplier_name, supplier_address, contact_number)

    @strawberry.mutation
    def delete_supplier(self, info, supplier_id: int) -> SupplierSchema:
        return delete_supplier(supplier_id)

    @strawberry.mutation
    def create_stock(self, info, product_id: int, quantity: int, location: str) -> StockSchema:
        return create_stock(product_id, quantity, location)

    @strawberry.mutation
    def update_stock(self, info, stock_id: int, product_id: int, quantity: int, location: str) -> StockSchema:
        return update_stock(stock_id, product_id, quantity, location)

    @strawberry.mutation
    def delete_stock(self, info, stock_id: int) -> StockSchema:
        return delete_stock(stock_id)

    @strawberry.mutation
    def create_consumer(self, info, consumer_name: str, consumer_address: str, contact_number: str) -> ConsumerSchema:
        return create_consumer(consumer_name, consumer_address, contact_number)

    @strawberry.mutation
    def update_consumer(
        self,
        info,
        consumer_id: int,
        consumer_name: str,
        consumer_address: str,
        contact_number: str,
    ) -> ConsumerSchema:
        return update_consumer(consumer_id, consumer_name, consumer_address, contact_number)

    @strawberry.mutation
    def delete_consumer(self, info, consumer_id: int) -> ConsumerSchema:
        return delete_consumer(consumer_id)

    @strawberry.mutation
    def create_product(self, info, product_name: str, amount: float, description: str) -> ProductSchema:
        return create_product(product_name, amount, description)

    @strawberry.mutation
    def update_product(self, info, product_id: int, product_name: str, amount: float, description: str) -> ProductSchema:
        return update_product(product_id, product_name, amount, description)

    @strawberry.mutation
    def delete_product(self, info, product_id: int) -> ProductSchema:
        return delete_product(product_id)

    @strawberry.mutation
    def create_supplier_order(
        self,
        info,
        supplier_id: int,
        stock_id: int,
        order_date: datetime,
        quantity: int,
    ) -> SupplierOrderSchema:
        return create_supplier_order(supplier_id, stock_id, order_date, quantity)

    @strawberry.mutation
    def update_supplier_order(
        self,
        info,
        order_id: int,
        supplier_id: int,
        stock_id: int,
        order_date: datetime,
        quantity: int,
    ) -> SupplierOrderSchema:
        return update_supplier_order(order_id, supplier_id, stock_id, order_date, quantity)

    @strawberry.mutation
    def delete_supplier_order(self, info, order_id: int) -> SupplierOrderSchema:
        return delete_supplier_order(order_id)

    @strawberry.mutation
    def create_consumer_order(
        self,
        info,
        consumer_id: int,
        product_id: int,
        order_date: datetime,
        quantity: int,
    ) -> ConsumerOrderSchema:
        return create_consumer_order(consumer_id, product_id, order_date, quantity)

    @strawberry.mutation
    def update_consumer_order(
        self,
        info,
        order_id: int,
        consumer_id: int,
        product_id: int,
        order_date: datetime,
        quantity: int,
    ) -> ConsumerOrderSchema:
        return update_consumer_order(order_id, consumer_id, product_id, order_date, quantity)

    @strawberry.mutation
    def delete_consumer_order(self, info, order_id: int) -> ConsumerOrderSchema:
        return delete_consumer_order(order_id)

    @strawberry.mutation
    def create_supplier_transaction(
        self,
        info,
        supplier_id: int,
        order_id: int,
        transaction_date: datetime,
    ) -> SupplierTransactionSchema:
        return create_supplier_transaction(order_id, supplier_id, transaction_date)

    @strawberry.mutation
    def update_supplier_transaction(
        self,
        info,
        transaction_id: int,
        supplier_id: int,
        order_id: int,
        transaction_date: datetime,
    ) -> SupplierTransactionSchema:
        return update_supplier_transaction(transaction_id, order_id, supplier_id, transaction_date)

    @strawberry.mutation
    def delete_supplier_transaction(self, info, transaction_id: int) -> SupplierTransactionSchema:
        return delete_supplier_transaction(transaction_id)

    @strawberry.mutation
    def create_consumer_transaction(
        self,
        info,
        consumer_id: int,
        order_id: int,
        stock_id: int,
        transaction_date: datetime,
    ) -> ConsumerTransactionSchema:
        return create_consumer_transaction(consumer_id, order_id, stock_id, transaction_date)

    @strawberry.mutation
    def update_consumer_transaction(
        self,
        info,
        transaction_id: int,
        consumer_id: int,
        order_id: int,
        stock_id: int,
        transaction_date: datetime,
    ) -> ConsumerTransactionSchema:
        return update_consumer_transaction(transaction_id, consumer_id, order_id, stock_id, transaction_date)

    @strawberry.mutation
    def delete_consumer_transaction(self, info, transaction_id: int) -> ConsumerTransactionSchema:
        return delete_consumer_transaction(transaction_id)


# Define the GraphQL schema
schema = strawberry.Schema(query=Query, mutation=Mutation)
