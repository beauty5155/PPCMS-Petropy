# from errors import DEFAULT_REFID
from ppcmslib.common import customError
from flask import request
from flask_restful import Resource
from model.account import Account, accountSchemaList

"""*******************************************
    Method to create Tenant
*******************************************"""
def createAccount(date, b_qty, b_rate, b_total, s_qty, s_rate, s_total, r_qty, profit):
    # account = Account.query.filter(Account.b_qty == b_qty).first()

    # if (account is None):    
    account = Account(date, b_qty, b_rate, b_total, s_qty, s_rate, s_total, r_qty, profit)
    account.saveRecord()

    return account


"""*******************************************
    Resource for Account API
*******************************************"""
class AccountResource(Resource):

    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    API for reading Account
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
    def get(self):
        appResponse = {}
        try:
            accountList =  Account.query.all()
            if (accountList is None):
                ceDict = customError('REG_CUSTOMER_NOT_FOUND', 'aaa')
                appResponse['errinfo'] = ceDict
            else:
                ceDict = customError('SUCCESS', 'Account')
                appResponse['errinfo'] = ceDict
                appResponse['account'] = accountSchemaList.dump(accountList)

        except Exception as error:
            ceDict = customError('GENERAL_ERROR', 'Account', str(error))
            appResponse['errinfo'] = ceDict

        return appResponse

    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Resourse for Login User API
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""

    def post(self):
        appResponse = {}
        accountInfo = request.get_json()
        print(accountInfo)

        try:
            date = accountInfo['date']
            b_qty = accountInfo['b_qty']
            b_rate = accountInfo['b_rate']
            # b_total = accountInfo['b_total']
            s_qty = accountInfo['s_qty']
            s_rate = accountInfo['s_rate']
            # s_total = accountInfo['s_total']
            # r_qty = accountInfo['r_qty']
            # profit = accountInfo['profit']

            n_b_qty = float(b_qty)
            n_b_rate = float(b_rate)
            b_total = (n_b_qty * n_b_rate)
            n_s_qty = float(s_qty)
            n_s_rate = float(s_rate)

            s_total = (n_s_qty * n_s_rate)
            r_qty = n_b_qty - n_s_qty
            profit = b_total - (r_qty * n_b_rate)
            # profit = 
            

            # account = Account.query.filter(Account.b_qty == b_qty).first()
            # print(account)

            # if account is not None:
            #     ceDict = customError('ACCOUNT_CALCULATION_IS_DONE', b_qty)
            #     appResponse['errinfo'] = ceDict
            # else:
            account = createAccount(date, b_qty, b_rate, b_total, s_qty, s_rate, s_total, r_qty, profit)
            ceDict = customError('SUCCESS', account.b_qty)
            appResponse['errinfo'] = ceDict
                

        except Exception as error:
            ceDict = customError('GENERAL_ERROR', 'account', str(error))
            appResponse['errinfo'] = ceDict

        return appResponse