from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

DATABASE_URI = "postgresql://postgres:database@database-1.cqv5dapod8ah.us-east-1.rds.amazonaws.com:5432/sms_lambda"
# Create the engine
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session=Session()
def init_db(app):
    app.cli.add_command(init_database)



def init_database():
    from models import Consumer, Supplier, Product, Stock, ConsumerOrder, SupplierOrder, ConsumerTransaction, SupplierTransaction
    session = Session()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session.commit()
    session.close()
