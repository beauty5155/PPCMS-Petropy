from db import alchemy
from db import marsh
# from model.app_base import AppBase
from marshmallow import fields
from datetime import timezone
import datetime


class Sales(alchemy.Model):
    __tablename__ = "sales"
    bill_no = alchemy.Column('bill_no', alchemy.Integer, primary_key=True)
    cid = alchemy.Column('cid', alchemy.Integer)
    rate = alchemy.Column('rate', alchemy.Integer)
    quantity = alchemy.Column('quantity', alchemy.Integer)
    total_amount = alchemy.Column('total_amount', alchemy.Integer)
    date = alchemy.Column('date', alchemy.DateTime)
    paid_amount = alchemy.Column('paid_amount', alchemy.Integer)
    balance_amount = alchemy.Column('balance_amount', alchemy.Integer)
    

    def __init__(self, cid, date, rate, quantity, total_amount, paid_amount, balance_amount):

        self.cid = cid
        self.date = date
        self.rate = rate
        self.quantity = quantity
        self.total_amount = total_amount
        self.paid_amount = paid_amount
        self.balance_amount = balance_amount
        # self.date = datetime.datetime.now(timezone.utc)
    
    def saveRecord(self):
        alchemy.session.add(self)
        alchemy.session.commit()

class SalesSchema(marsh.Schema):

    class Meta:
        ordered = True
        fields = ("bill_no", "cid", "date", "rate", "quantity", "total_amount", "paid_amount", "paid_amount", "balance_amount")


salesSchema = SalesSchema()
salesSchemaList  = SalesSchema(many=True)
