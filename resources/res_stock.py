from flask import request
from ppcmslib.common import customError
from flask_restful import Resource
from model.stock import Stock, stockSchemaList


"""*******************************************
    Method to create Stock
*******************************************"""
def createStock(date, m_reading, e_reading, purchase_qty, remaining_qty):
    # stock = Stock.query.filter(Stock.m_reading == m_reading).first()

    # if (stock is None):    
    stock = Stock(date, m_reading, e_reading, purchase_qty, remaining_qty)
    stock.saveRecord()

    return stock


"""*******************************************
    Resource for Stock API
*******************************************"""
class StockResource(Resource):

    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    API for reading Stock
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
    def get(self):
        appResponse = {}
        try:
            stockList =  Stock.query.all()
            if (stockList is None):
                ceDict = customError('REG_CUSTOMER_NOT_FOUND', 'aaa')
                appResponse['errinfo'] = ceDict
            else:
                ceDict = customError('SUCCESS', 'Stock')
                appResponse['errinfo'] = ceDict
                appResponse['stock'] = stockSchemaList.dump(stockList)

        except Exception as error:
            ceDict = customError('GENERAL_ERROR', 'Stock', str(error))
            appResponse['errinfo'] = ceDict

        return appResponse

    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    API for creating Customer
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
    def post(self):
        appResponse = {}
        stockInfo = request.get_json()
        # printData(stockInfo)

        try:
            date = stockInfo['date']
            m_reading = stockInfo['m_reading']
            e_reading = stockInfo['e_reading']
            purchase_qty = stockInfo['purchase_qty']
            remaining_qty = stockInfo['remaining_qty']
# type--> petrol/diesel

            # stock = Stock.query.filter(Stock.m_reading == m_reading).first()
            # if (stock is not None):
            #     ceDict = customError('STOCK_ORDER_ALREADY_DONE', stock.m_reading)
            #     appResponse['errinfo'] = ceDict
            # else:
            stock = createStock(date, m_reading, e_reading, purchase_qty, remaining_qty)
            ceDict = customError('SUCCESS', stock.order_id)
            appResponse['errinfo'] = ceDict

        except Exception as error:
            ceDict = customError('GENERAL_ERROR', 'aaa', str(error))
            appResponse['errinfo'] = ceDict

        return appResponse
