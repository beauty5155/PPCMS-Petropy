from db import alchemy
from db import marsh
# from model.app_base import AppBase
from marshmallow import fields
from datetime import timezone
import datetime


class Account(alchemy.Model):
    __tablename__ = "account"
    aid = alchemy.Column('aid', alchemy.Integer, primary_key=True)
    date = alchemy.Column('date', alchemy.DateTime)
    b_qty = alchemy.Column('b_qty', alchemy.Integer)
    b_rate = alchemy.Column('b_rate', alchemy.Float)
    b_total = alchemy.Column('b_total', alchemy.Float)
    s_qty = alchemy.Column('s_qty', alchemy.Integer)
    s_rate = alchemy.Column('s_rate', alchemy.Float)
    s_total = alchemy.Column('s_total', alchemy.Float)
    r_qty = alchemy.Column('r_qty', alchemy.Integer)
    profit = alchemy.Column('profit', alchemy.Float)

    def __init__(self, date, b_qty, b_rate, b_total, s_qty, s_rate, s_total, r_qty, profit):
        self.date = date
        self.b_qty = b_qty
        self.b_rate = b_rate
        self.b_total = b_total
        self.s_qty = s_qty
        self.s_rate = s_rate
        self.s_total = s_total
        self.r_qty = r_qty
        self.profit = profit
        
        # self.date = datetime.datetime.now(timezone.utc)
    
    def saveRecord(self):
        alchemy.session.add(self)
        alchemy.session.commit()

class AccountSchema(marsh.Schema):

    class Meta:
        ordered = True
        fields = ("aid", "date", "b_qty", "b_rate", "b_total", "s_qty", "s_rate", "s_total", "r_qty", "profit")


accountSchema = AccountSchema()
accountSchemaList  = AccountSchema(many=True)
