import databases
import sqlalchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///my_hw_database.db"
database = databases.Database(DATABASE_URL)

# Base = declarative_base()

db = databases.Database(DATABASE_URL)
mdt = sqlalchemy.MetaData()
users_db = sqlalchemy.Table( "users", mdt,
                        sqlalchemy.Column("id", sqlalchemy.Integer,primary_key=True),
                        sqlalchemy.Column("login", sqlalchemy.String(32)),
                        sqlalchemy.Column("password", sqlalchemy.String(64)),
                        sqlalchemy.Column("email", sqlalchemy.String(128)),
                        )

product_db = sqlalchemy.Table( "products", mdt,
                        sqlalchemy.Column("id", sqlalchemy.Integer,primary_key=True),
                        sqlalchemy.Column("name", sqlalchemy.String(32)),
                        sqlalchemy.Column("description", sqlalchemy.String(1000)),
                        sqlalchemy.Column("price", sqlalchemy.Float()),
                        )

order_db = sqlalchemy.Table( "orders", mdt,
                        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                        sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'),
                                          nullable=False),
                        sqlalchemy.Column("product_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'),
                                          nullable=False),
                        sqlalchemy.Column("order_status", sqlalchemy.Boolean),
                        sqlalchemy.Column("order_date", sqlalchemy.DateTime),
                        )

engine = sqlalchemy.create_engine(DATABASE_URL,
    connect_args={"check_same_thread": False})
mdt.create_all(engine)
