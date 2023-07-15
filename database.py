from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import scoped_session

Base = declarative_base()

DATABASE_URI = "postgresql://postgres:database@database-1.cqv5dapod8ah.us-east-1.rds.amazonaws.com:5432/sms_lambda"
# Create the engine
engine = create_engine(DATABASE_URI)

Base.metadata.create_all(engine)
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))
