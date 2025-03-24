from db import alchemy
from db import marsh
# from model.app_base import AppBase
from marshmallow import fields

class Stock(alchemy.Model):
    __tablename__ = "stock"
    order_id = alchemy.Column('order_id', alchemy.Integer, primary_key=True)
    date = alchemy.Column('date', alchemy.DateTime)
    m_reading = alchemy.Column('m_reading', alchemy.Integer)
    e_reading = alchemy.Column('e_reading', alchemy.Integer)
    purchase_qty = alchemy.Column('purchase_qty', alchemy.Integer)
    remaining_qty = alchemy.Column('remaining_qty', alchemy.Integer)

    def __init__(self, date, m_reading, e_reading, purchase_qty, remaining_qty):
        self.m_reading = m_reading
        self.e_reading = e_reading
        self.purchase_qty = purchase_qty
        self.remaining_qty = remaining_qty
        self.date = date
    
    def saveRecord(self):
        alchemy.session.add(self)
        alchemy.session.commit()

class StockSchema(marsh.Schema):

    class Meta:
        ordered = True
        fields = ("order_id", "date", "m_reading", "e_reading", "purchase_qty", "remaining_qty")


stockSchema = StockSchema()
stockSchemaList  = StockSchema(many=True)
