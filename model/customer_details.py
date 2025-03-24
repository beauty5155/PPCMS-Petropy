from db import alchemy
from db import marsh
# from model.app_base import AppBase
from marshmallow import fields
from datetime import timezone
import datetime


class CustomerDetails(alchemy.Model):
    __tablename__ = "customer_details"
    cid = alchemy.Column('cid', alchemy.Integer, primary_key=True)
    name = alchemy.Column('name', alchemy.String)
    password = alchemy.Column('password', alchemy.String)
    phone = alchemy.Column('phone', alchemy.Integer)
    address = alchemy.Column('address', alchemy.String)
    joining_date = alchemy.Column('joining_date', alchemy.DateTime)
    balance = alchemy.Column('balance', alchemy.Float)
    max_value = alchemy.Column('max_value', alchemy.Integer)
    

    def __init__(self, name, password, phone, address, balance, max_value):

        self.name = name
        self.password = password
        self.phone = phone
        self.address = address
        self.balance = balance
        self.max_value = max_value
        self.joining_date = datetime.datetime.now(timezone.utc)

    def saveRecord(self):
        alchemy.session.add(self)
        alchemy.session.commit()

class CustomerDetailsSchema(marsh.Schema):

    class Meta:
        ordered = True
        fields = ("cid", "name", "phone", "address", "balance", "max_value", "joining_date")


customerDetailsSchema = CustomerDetailsSchema()
customerDetailsSchemaList  = CustomerDetailsSchema(many=True)


"""************************************************************************************************
    Login Schema 
************************************************************************************************"""
class LoginSchema(marsh.Schema):
    class Meta:
        fields = ("name", "password")


loginSchema = LoginSchema()
loginSchemaList = LoginSchema(many=True)
