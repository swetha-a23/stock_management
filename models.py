from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, create_engine, DateTime, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine("postgresql+psycopg2://postgres:admin123@localhost:5432/project_stock")
Base.metadata.bind = engine


class Supplier(Base):
    __tablename__ = 'supplier'

    supplier_id = Column(Integer, primary_key=True)
    supplier_name = Column(String(255))
    supplier_address = Column(String(255))
    contact_number = Column(String)

    products = relationship("Product", back_populates="supplier")
    supplier_orders = relationship("SupplierOrder", backref="supplier")
    supplier_transactions = relationship("SupplierTransaction", backref="supplier")


class Product(Base):
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(255))
    amount = Column(Numeric(10, 2))
    description = Column(String)

    supplier_id = Column(Integer, ForeignKey('supplier.supplier_id'))
    supplier = relationship("Supplier", back_populates="products")
    stocks = relationship("Stock", backref="product")
    consumer_orders = relationship("ConsumerOrder", backref="product")


class Stock(Base):
    __tablename__ = 'stock'

    stock_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.product_id'))
    quantity = Column(Integer)
    location = Column(String)

    supplier_orders = relationship("SupplierOrder", backref="stock")
    consumer_transactions = relationship("ConsumerTransaction", backref="stock")


class Consumer(Base):
    __tablename__ = 'consumer'

    consumer_id = Column(Integer, primary_key=True)
    consumer_name = Column(String(255))
    consumer_address = Column(String(255))
    contact_number = Column(String)

    consumer_orders = relationship("ConsumerOrder", backref="consumer")
    consumer_transactions = relationship("ConsumerTransaction", backref="consumer")


class SupplierOrder(Base):
    __tablename__ = 'supplier_order'

    order_id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey('supplier.supplier_id'))
    stock_id = Column(Integer, ForeignKey('stock.stock_id'))
    order_date = Column(DateTime)
    quantity = Column(Integer)
    total_amount = Column(Numeric(10, 2))

    def calculate_total_price(self):
        if self.product:
            self.total_amount = self.quantity * self.product.amount


class ConsumerOrder(Base):
    __tablename__ = 'consumer_order'

    order_id = Column(Integer, primary_key=True)
    consumer_id = Column(Integer, ForeignKey('consumer.consumer_id'))
    product_id = Column(Integer, ForeignKey('product.product_id'))
    order_date = Column(DateTime)
    quantity = Column(Integer)
    total_amount = Column(Numeric(10, 2))

    def calculate_total_price(self):
        if self.product:
            self.total_amount = self.quantity * self.product.amount


class SupplierTransaction(Base):
    __tablename__ = 'supplier_transaction'

    transaction_id = Column(Integer, primary_key=True, nullable=False)
    supplier_id = Column(Integer, ForeignKey('supplier.supplier_id'))
    order_id = Column(Integer, ForeignKey('supplier_order.order_id'))
    amount = Column(Numeric(10, 2), nullable=False)
    transaction_date = Column(DateTime, nullable=False)

    supplier_order = relationship('SupplierOrder', backref='supplier_transactions')

    def set_amount_from_order(self):
        if self.order_id:
            self.amount = SupplierOrder.total_amount


class ConsumerTransaction(Base):
    __tablename__ = 'consumer_transaction'

    transaction_id = Column(Integer, primary_key=True)
    consumer_id = Column(Integer, ForeignKey('consumer.consumer_id'))
    stock_id = Column(Integer, ForeignKey('stock.stock_id'))
    order_id = Column(Integer, ForeignKey('consumer_order.order_id'))
    transaction_date = Column(DateTime)
    amount = Column(Numeric(10, 2), nullable=False)

    consumer_order = relationship('ConsumerOrder', backref='consumer_transactions')


    def set_amount_from_order(self):
        if self.order_id:
            self.amount = ConsumerOrder.total_amount


if __name__ == '__main__':
    Base.metadata.create_all(engine)
