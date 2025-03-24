from operator import and_
from db import alchemy
from db import marsh
from datetime import timezone
import datetime

from model.customer_details import CustomerDetails


class Payment(alchemy.Model):
    __tablename__ = "payment"
    pid = alchemy.Column('pid', alchemy.Integer, primary_key=True)
    cid = alchemy.Column('cid', alchemy.Integer)
    date = alchemy.Column('date', alchemy.DateTime)
    paid_amount = alchemy.Column('paid_amount', alchemy.Integer)

    def __init__(self, cid, date, paid_amount):
        self.cid = cid
        self.date = date
        self.paid_amount = paid_amount

    def saveRecord(self):
        alchemy.session.add(self)
        alchemy.session.commit()

class PaymentSchema(marsh.Schema):

    class Meta:
        ordered = True
        fields = ("pid", "cid", "date", "paid_amount")


paymentSchema = PaymentSchema()
paymentSchemaList  = PaymentSchema(many=True)
