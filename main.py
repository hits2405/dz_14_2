import json

import Datetime as Datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


# установка - pip install flask sqlalchemy flask-sqlalchemy
db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dz_14_2.db"




class Users(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    email = Column(String)
    role = Column(String)
    phone = Column(String)


class Offer(db.Model):
    __tablename__ = "offer"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    executor_id = Column(Integer)


class Order(db.Model):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    start_date = Column(Datetime)
    end_date = Column(Datetime)
    adderss = Column(String)
    price = Column(Integer)
    customer_id = Column(Integer)
    executor_id = Column(Integer)


# db.drop_all()  # удалит данные
db.create_all()

if __name__ == '__main__':
    print_hi('PyCharm')
