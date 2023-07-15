from schemas import *
import json
from database import init_database

init_database()

def lambda_handler(event, context):
    print(event)
    
    if event.get('info').get('fieldName') == 'getSupplierById':
        return Query().get_supplier_by_id(event.get('arguments').get('supplier_id'))
    
    elif event.get('info').get('fieldName') == 'getAllSuppliers':
        return Query().get_all_suppliers()
    
    elif event.get('info').get('fieldName') == 'getStockById':
        return Query().get_stock_by_id(event.get('arguments').get('stock_id'))
    
    elif event.get('info').get('fieldName') == 'getAllStocks':
        return Query().get_all_stocks()
    
    elif event.get('info').get('fieldName') == 'getConsumerById':
        return Query().get_consumer_by_id(event.get('arguments').get('consumer_id'))
    
    elif event.get('info').get('fieldName') == 'getAllConsumers':
        return Query().get_all_consumers()
    
    
    elif event.get('info').get('fieldName') == 'getProductById':
        return Query().get_product_by_id(event.get('arguments').get('product_id'))
    
    elif event.get('info').get('fieldName') == 'getAllProducts':
        return Query().get_all_products()
    
    
    elif event.get('info').get('fieldName') == 'getSupplierOrderById':
        return Query().get_supplier_order_by_id(event.get('arguments').get('order_id'))
    
    elif event.get('info').get('fieldName') == 'getAllSupplierOrders':
        return Query().get_all_supplier_orders()
    
    elif event.get('info').get('fieldName') == 'get_orders_by_supplier_id':
        return Query().get_orders_by_supplier_id(event.get('arguments').get('supplier_id'))
    
    elif event.get('info').get('fieldName') == 'get_suppliers_by_order_id':
        return Query().get_suppliers_by_order_id(event.get('arguments').get('order_id'))
    
    
    
    elif event.get('info').get('fieldName') == 'getConsumerOrderById':
        return Query().get_consumer_order_by_id(event.get('arguments').get('order_id'))
    
    elif event.get('info').get('fieldName') == 'getAllConsumerOrders':
        return Query().get_all_consumer_orders()
    
    elif event.get('info').get('fieldName') == 'get_orders_by_consumer_id':
        return Query().get_orders_by_consumer_id(event.get('arguments').get('consumer_id'))
    
    elif event.get('info').get('fieldName') == 'get_consumers_by_order_id':
        return Query().get_consumers_by_order_id(event.get('arguments').get('order_id'))
    
    elif event.get('info').get('fieldName') == 'getSupplierTransactionById':
        return Query().get_supplier_transaction_by_id(event.get('arguments').get('transaction_id'))
    
    elif event.get('info').get('fieldName') == 'getAllSupplierTransactions':
        return Query().get_all_supplier_transactions()
    
    elif event.get('info').get('fieldName') == 'get_transactions_by_supplier_id':
        return Query().get_transactions_by_supplier_id(event.get('arguments').get('supplier_id'))
    
    elif event.get('info').get('fieldName') == 'get_supplier_by_transaction_id':
        return Query().get_supplier_by_transaction_id(event.get('arguments').get('transaction_id'))
    
    elif event.get('info').get('fieldName') == 'get_Supplierorder_by_transaction_id':
        return Query().get_Supplierorder_by_transaction_id(event.get('arguments').get('transaction_id'))
    
    elif event.get('info').get('fieldName') == 'get_Suppliertransaction_by_order_id':
        return Query().get_Suppliertransaction_by_order_id(event.get('arguments').get('order_id'))
    
    elif event.get('info').get('fieldName') == 'getConsumerTransactionById':
        return Query().get_consumer_transaction_by_id(event.get('arguments').get('transaction_id'))
    
    elif event.get('info').get('fieldName') == 'getAllConsumerTransactions':
        return Query().get_all_consumer_transactions()
    
    elif event.get('info').get('fieldName') == 'get_transactions_by_consumer_id':
        return Query().get_transactions_by_consumer_id(event.get('arguments').get('consumer_id'))
    
    elif event.get('info').get('fieldName') == 'get_consumer_by_transaction_id':
        return Query().get_consumer_by_transaction_id(event.get('arguments').get('transaction_id'))
    
    elif event.get('info').get('fieldName') == 'get_Consumerorder_by_transaction_id':
        return Query().get_Consumerorder_by_transaction_id(event.get('arguments').get('transaction_id'))
    
    elif event.get('info').get('fieldName') == 'get_Consumertransaction_by_order_id':
        return Query().get_Consumertransaction_by_order_id(event.get('arguments').get('order_id'))
    
    elif event.get('info').get('fieldName') == 'create_supplier':
        return Mutation.create_supplier(
            event.get('arguments').get('supplier_name'),
            event.get('arguments').get('supplier_address'),
            event.get('arguments').get('contact_number')
      
        )
    
    elif event.get('info').get('fieldName') == 'update_supplier':
        return Mutation.update_supplier(
            event.get('arguments').get('supplier_id'),
            event.get('arguments').get('supplier_name'),
            event.get('arguments').get('asupplier_address'),
            event.get('arguments').get('contact_number')
        )
    
    elif event.get('info').get('fieldName') == 'delete_supplier':
        return Mutation.delete_supplier(event.get('arguments').get('supplier_id'))
    
    elif event.get('info').get('fieldName') == 'create_stock':
        return Mutation().create_stock(
            event.get('arguments').get('product_id'),
            event.get('arguments').get('quantity'),
            event.get('arguments').get('location')
            
        )
    
    elif event.get('info').get('fieldName') == 'update_stock':
        return Mutation().update_stock(
            event.get('arguments').get('stock_id'),
            event.get('arguments').get('product_id'),
            event.get('arguments').get('quantity'),
            event.get('arguments').get('location')
            
        )
    
    elif event.get('info').get('fieldName') == 'delete_stock':
        return Mutation().delete_stock(event.get('arguments').get('stock_id'))
    
    elif event.get('info').get('fieldName') == 'create_consumer':
        return Mutation().create_consumer(
            event.get('arguments').get('consumer_name'),
            event.get('arguments').get('consumer_address'),
            event.get('arguments').get('contact_number')
        )
    
    elif event.get('info').get('fieldName') == 'update_consumer':
        return Mutation().update_consumer(
            event.get('arguments').get('consumer_id'),
            event.get('arguments').get('consumer_name'),
            event.get('arguments').get('consumer_address'),
            event.get('arguments').get('contact_number')
        )
    
    elif event.get('info').get('fieldName') == 'delete_consumer':
        return Mutation().delete_consumer(event.get('arguments').get('consumer_id')
        )
    
    
    elif event.get('info').get('fieldName') == 'create_product':
        return Mutation.create_product(
            event.get('arguments').get('product_name'),
            event.get('arguments').get('amount'),
            event.get('arguments').get('description')
        )
    
    elif event.get('info').get('fieldName') == 'update_product':
        return Mutation.update_product(
            event.get('arguments').get('product_id'),
            event.get('arguments').get('product_name'),
            event.get('arguments').get('amount'),
            event.get('arguments').get('description')
        )
    
    elif event.get('info').get('fieldName') == 'delete_product':
        return Mutation.delete_product(event.get('arguments').get('product_id'))
    
    
    elif event.get('info').get('fieldName') == 'create_supplier_order':
        return Mutation().create_supplier_order(
            event.get('arguments').get('supplier_id'),
            event.get('arguments').get('stock_id'),
            event.get('arguments').get('order_date'),
            event.get('arguments').get('quantity')
        )
    
    elif event.get('info').get('fieldName') == 'update_supplier_order':
        return Mutation().update_supplier_order(
            event.get('arguments').get('order_id'),
            event.get('arguments').get('supplier_id'),
            event.get('arguments').get('stock_id'),
            event.get('arguments').get('order_date'),
            event.get('arguments').get('quantity')
        )
    
    elif event.get('info').get('fieldName') == 'delete_supplier_order':
        return Mutation().delete_supplier_order(event.get('arguments').get('order_id'))
    
    
    
    elif event.get('info').get('fieldName') == 'create_consumer_order':
        return Mutation().create_consumer_order(
            event.get('arguments').get('consumer_id'),
            event.get('arguments').get('product_id'),
            event.get('arguments').get('order_date'),
            event.get('arguments').get('quantity')
        )
    
    elif event.get('info').get('fieldName') == 'update_consumer_order':
        return Mutation().update_consumer_order(
            event.get('arguments').get('order_id'),
            event.get('arguments').get('consumer_id'),
            event.get('arguments').get('product_id'),
            event.get('arguments').get('order_date'),
            event.get('arguments').get('quantity')
        )
    
    elif event.get('info').get('fieldName') == 'delete_consumer_order':
        return Mutation().delete_consumer_order(event.get('arguments').get('order_id'))
    
    elif event.get('info').get('fieldName') == 'create_supplier_transaction':
        return Mutation().create_supplier_transaction(
            event.get('arguments').get('supplier_id'),
            event.get('arguments').get('order_id'),
            event.get('arguments').get('transaction_date')
        )
    
    elif event.get('info').get('fieldName') == 'update_supplier_transaction':
        return Mutation().update_supplier_transaction(
            event.get('arguments').get('transaction_id'),
            event.get('arguments').get('order_id'),
            event.get('arguments').get('supplier_id'),
            event.get('arguments').get('transaction_date')
        )
    
    elif event.get('info').get('fieldName') == 'delete_supplier_transaction':
        return Mutation().delete_supplier_transaction(event.get('arguments').get('transaction_id'))
    
    elif event.get('info').get('fieldName') == 'create_consumer_transaction':
        return Mutation().create_consumer_transaction(
            event.get('arguments').get('consumer_id'),
            event.get('arguments').get('order_id'),
            event.get('arguments').get('stock_id'),
            event.get('arguments').get('transaction_date')
        )
    
    elif event.get('info').get('fieldName') == 'update_consumer_transaction':
        return Mutation().update_consumer_transaction(
            event.get('arguments').get('transaction_id'),
            event.get('arguments').get('consumer_id'),
            event.get('arguments').get('order_id'),
            event.get('arguments').get('stock_id'),
            event.get('arguments').get('transaction_date')
        )
    
    elif event.get('info').get('fieldName') == 'delete_consumer_transaction':
        return Mutation().delete_consumer_transaction(event.get('arguments').get('transaction_id'))