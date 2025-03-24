from flask import request
from model.customer_details import CustomerDetails
from model.sales import Sales
from ppcmslib.common import customError
from flask_restful import Resource
from model.payment import Payment, paymentSchemaList, paymentSchema


"""*******************************************
    Method to create Payment
*******************************************"""
def createPayment(cid, date, paid_amount):
    # payment = Payment.query.filter(Payment.cid == cid).first()

    # if (payment is None):
    payment = Payment(cid, date, paid_amount)
    payment.saveRecord()

    return payment


"""*******************************************
    Resource for Payment API
*******************************************"""
class PaymentResource(Resource):

    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    API for reading Payment
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
    # def get(self):
    #     appResponse = {}
    #     try:
    #         paymentList =  Payment.query.all()
    #         if (paymentList is None):
    #             ceDict = customError('REG_CUSTOMER_NOT_FOUND', 'Payment')
    #             appResponse['errinfo'] = ceDict
    #         else:
    #             ceDict = customError('SUCCESS', 'Payment')
    #             appResponse['errinfo'] = ceDict
    #             appResponse['payment'] = paymentSchemaList.dump(paymentList)

    def get(self):
        appResponse = {}
        qry_params = request.args
        qrList = qry_params.to_dict()
        # qrList = request.get_json()

        try:
            flag = qrList['flag'].upper()

            if (flag == 'PAYMENT_ALL'):
                paymentList =  Payment.query.all()
                ceDict = customError('SUCCESS', 'Payment')
                appResponse['errinfo'] = ceDict

            elif (flag == 'PAYMENT_W_CID'):
                cid = qrList['cid']
                paymentList = Payment.query.filter(Payment.cid == cid).all()
                ceDict = customError('SUCCESS', 'Payment')
                appResponse['errinfo'] = ceDict
    
            appResponse['payment'] = paymentSchemaList.dump(paymentList)

        except Exception as error:
            ceDict = customError('GENERAL_ERROR', 'Payment', str(error))
            appResponse['errinfo'] = ceDict

        return appResponse


    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    API for creating Payment
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
    def post(self):
        appResponse = {}
        paymentInfo = request.get_json()
        print(paymentInfo, " <-- paymentInfo")

        try:
            cid = paymentInfo['cid']
            date = paymentInfo['date']
            paid_amount = paymentInfo['paid_amount']

            payment = Payment.query.filter(Payment.cid != cid).first()
            if (payment is None):
                # impliment Customer does not exist logic---------------------->>>>>>>>>>>
                ceDict = customError('CUSTOMER_NOT_FOUND', cid)
                appResponse['errinfo'] = ceDict
            else:
                payment = createPayment(cid, date, paid_amount)
                if(payment.pid is not None):
                    remaining_balance = 0
                    cusList =  CustomerDetails.query.filter(CustomerDetails.cid == cid).first()

                    remaining_balance = int(cusList.balance) - int(paid_amount)
                    cusList.balance = remaining_balance
                    cusList.saveRecord()

                    

                    ceDict = customError('SUCCESS', cid)
                    appResponse['errinfo'] = ceDict

        except Exception as error:
            ceDict = customError('GENERAL_ERROR', 'bbb', str(error))
            appResponse['errinfo'] = ceDict

        return appResponse


"""************************************
Resourse for single Payment
************************************"""
class PaymentSingleResource(Resource):
    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    API for reading single Payment
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
    def get(self, cid):
        appResponse = {}
        try:
            payment = Payment.query.get(cid)
            ceDict = customError('SUCCESS', 'Payment')
            appResponse['errinfo'] = ceDict
            appResponse['payment'] = paymentSchema.dump(payment)

        except Exception as error:
            ceDict = customError('GENERAL_ERROR', 'aaa', str(error))
            appResponse['errinfo'] = ceDict

        return appResponse