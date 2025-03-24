# from errors import DEFAULT_REFID
from ppcmslib.common import customError
from flask import request
from flask_restful import Resource
# from model.tnt_package import TNTPackage, tntPkgSchemaList, tntPkgSchema
# import constant
from sqlalchemy import and_
import hashlib
from model.customer_details import CustomerDetails, customerDetailsSchemaList, customerDetailsSchema, loginSchema


"""*******************************************
    Method to create Customer
*******************************************"""
def createCustomerDetails(name, newpass, phone, address, balance, max_value):
    customer = CustomerDetails.query.filter(CustomerDetails.name == name).first()

    if (customer is None):    
        customer = CustomerDetails(name, newpass, phone, address, balance, max_value)
        customer.saveRecord()

    return customer


"""*******************************************
    Resource for Customer API
*******************************************"""
class CustomerDetailsResource(Resource):

    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    API for reading Customer Details
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
    def get(self):
        appResponse = {}
        try:
            cusList =  CustomerDetails.query.all()
            if (cusList is None):
                ceDict = customError('CUSTOMER_NOT_FOUND', 'aaa')
                appResponse['errinfo'] = ceDict
            else:
                ceDict = customError('SUCCESS', 'Customer')
                appResponse['errinfo'] = ceDict
                appResponse['contact'] = customerDetailsSchemaList.dump(cusList)

        except Exception as error:
            ceDict = customError('GENERAL_ERROR', 'Customer', str(error))
            appResponse['errinfo'] = ceDict

        return appResponse


    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    API for creating Customer
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
    def post(self):
        appResponse = {}
        customerInfo = request.get_json()
        # printData(customerInfo)

        try:
            name = customerInfo['name']
            password = customerInfo['password']
            phone = customerInfo['phone']
            address = customerInfo['address']
            balance = customerInfo['balance']
            max_value = customerInfo['max_value']

            newpass = hashPassword(password)

            customer = CustomerDetails.query.filter(CustomerDetails.name == name).first()
            if (customer is not None):
                ceDict = customError('CUSTOMER_ALREADY_EXIST', customer.name)
                appResponse['errinfo'] = ceDict
            else:
                customer = createCustomerDetails(name, newpass, phone, address, balance, max_value)
                ceDict = customError('SUCCESS', customer.cid)
                appResponse['errinfo'] = ceDict

        except Exception as error:
            ceDict = customError('GENERAL_ERROR', 'aaa', str(error))
            appResponse['errinfo'] = ceDict

        return appResponse


    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        API for updating Customer
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""

    def put(self):
        appResponse = {}
        cusInfo = request.get_json()
        # printData(cusInfo)
        
        try:
            cid = cusInfo['cid']
            
            customer = CustomerDetails.query.get(cid)

            if (customer is None):
                ceDict = customError('CUSTOMER_NOT_FOUND', customer.cid)
                appResponse['errinfo'] = ceDict
            else:
                if ('cid' in cusInfo):
                    customer.cid = cusInfo['cid']

                if ('name' in cusInfo):
                    customer.name = cusInfo['name']

                if ('phone' in cusInfo):
                    customer.phone = cusInfo['phone']

                if ('address' in cusInfo):
                    customer.address = cusInfo['address']

                if ('balance' in cusInfo):
                    customer.balance = cusInfo['balance']
                
                if ('joining_date' in cusInfo):
                    customer.joining_date = cusInfo['joining_date']

                if ('max_value' in cusInfo):
                    customer.max_value = cusInfo['max_value']
  
                customer.saveRecord()
                ceDict = customError('SUCCESS', customer.cid)
                appResponse['errinfo'] = ceDict

        except Exception as error:
            ceDict = customError('GENERAL_ERROR', 'aaa', str(error))
            appResponse['errinfo'] = ceDict

        return appResponse



"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Resourse for Login customer API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
class LoginResource(Resource):
    def post(self):
        appResponse = []
        loginInfo = request.get_json()
        print(loginInfo)

        """----------------------------------------
        For security reason the password is not printed in log
        ----------------------------------------"""
        urInfoTemp = loginInfo.copy()
        urInfoTemp.pop('password')
        print('User Input', urInfoTemp)

        try:
            name = loginInfo['name']
            password = loginInfo['password']

            newpass = hashPassword(password)

            userLogin = CustomerDetails.query.filter(
                        CustomerDetails.name==name
                        # CustomerDetails.password==password
                    ).first()

            if userLogin is None:
                ceDict = customError('USER_NOT_FOUND', name)
                appResponse.append({"errinfo": ceDict})
            elif(newpass != userLogin.password):
                ceDict = customError('INCORRECT_PASSWORD', password)
                appResponse.append({"errinfo": ceDict})
            else:
                ceDict = customError('SUCCESS', userLogin.name)
                userLoginInfo = loginSchema.dump(userLogin)
                appResponse.append({"errinfo": ceDict, "user": userLoginInfo})

        except Exception as error:
            ceDict = customError('GENERAL_ERROR', 'login', str(error))
            appResponse.append({"errinfo": ceDict})

        return appResponse


"""************************************
Implimention of SHA512 for password
************************************"""
def hashPassword(pwd):
    encodedPwd = pwd.encode()
    pwd_sha3_512 = hashlib.sha3_512(encodedPwd)
    return pwd_sha3_512.hexdigest()


"""************************************
Resourse for single Contact
************************************"""
class CustomerDetailsSingleResource(Resource):

    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    API for reading single Contact
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
    def get(self, cid):
        appResponse = {}
        try:
            customer = CustomerDetails.query.get(cid)
            ceDict = customError('SUCCESS', 'Contact')
            appResponse['errinfo'] = ceDict
            appResponse['customer'] = customerDetailsSchema.dump(customer)

        except Exception as error:
            ceDict = customError('GENERAL_ERROR', 'aaa', str(error))
            appResponse['errinfo'] = ceDict

        return appResponse