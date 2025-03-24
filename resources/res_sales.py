from flask import request
from model.customer_details import CustomerDetails
from ppcmslib.common import customError
from flask_restful import Resource
from model.sales import Sales, salesSchemaList


"""*******************************************
    Method to create Sales
*******************************************"""
def createSales(cid, date, rate, quantity, total_amount, paid_amount, balance_amount):
    # sales = Sales.query.filter(Sales.cid == cid).first()

    # if (sales is None):    
    sales = Sales(cid, date, rate, quantity, total_amount, paid_amount, balance_amount)
    sales.saveRecord()

    return sales


"""*******************************************
    Resource for Sales API
*******************************************"""
class SalesResource(Resource):

    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    API for reading Sales
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
    def get(self):
        appResponse = {}
        try:
            salesList =  Sales.query.all()
            if (salesList is None):
                ceDict = customError('REG_CUSTOMER_NOT_FOUND', 'Sales')
                appResponse['errinfo'] = ceDict
            else:
                ceDict = customError('SUCCESS', 'Sales')
                appResponse['errinfo'] = ceDict
                appResponse['sales'] = salesSchemaList.dump(salesList)

        except Exception as error:
            ceDict = customError('GENERAL_ERROR', 'Sales', str(error))
            appResponse['errinfo'] = ceDict

        return appResponse


    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    API for creating Sales
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
    def post(self):
        appResponse = {}
        salesInfo = request.get_json()
        # printData(salesInfo)

        try:
            cid = salesInfo['cid']
            date = salesInfo['date']
            rate = salesInfo['rate']
            quantity = salesInfo['quantity']
            total_amount = salesInfo['total_amount']
            paid_amount = salesInfo['paid_amount']
            balance_amount = salesInfo['balance_amount']

            sales = createSales(cid, date, rate, quantity, total_amount, paid_amount, balance_amount)
            if(sales is not None):
                salesList =  Sales.query.filter(Sales.cid == cid).all()

                sum_balance_amount = 0
                for sale in salesList:
                    sum_balance_amount = sum_balance_amount + sale.balance_amount

                cusList =  CustomerDetails.query.filter(CustomerDetails.cid == cid).first()

                cusList.balance = sum_balance_amount
                cusList.saveRecord()

            ceDict = customError('SUCCESS', sales.cid)
            appResponse['errinfo'] = ceDict

        except Exception as error:
            ceDict = customError('GENERAL_ERROR', 'aaa', str(error))
            appResponse['errinfo'] = ceDict

        return appResponse

