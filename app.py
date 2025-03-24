# print("Hii, python's 1st print")

# def print_para(name):
#     print("hello", name)

# if __name__ == '__main__':
#     print_para('beauty')





# import mysql.connector
from db import alchemy, marsh
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import dbconfig
from resources.res_sales import SalesResource
from resources.res_account import AccountResource
from resources.res_payment import PaymentResource, PaymentSingleResource
from resources.res_stock import StockResource
from resources.res_customer_details import LoginResource, CustomerDetailsResource, CustomerDetailsSingleResource


app = Flask(__name__)

app.debug = DEBUG=True

cors = CORS(app)
api = Api(app)
alchemy.init_app(app)
marsh.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+dbconfig.username + \
    ':'+dbconfig.password+'@'+dbconfig.dbhost+'/'+dbconfig.database
# app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



api.add_resource(LoginResource, '/userlogin')
api.add_resource(CustomerDetailsResource, '/customer')
api.add_resource(CustomerDetailsSingleResource, '/customer/<int:cid>')

api.add_resource(AccountResource, '/account')

api.add_resource(PaymentResource, '/payment')
api.add_resource(PaymentSingleResource, '/payment/<int:cid>')

api.add_resource(StockResource, '/stock')

api.add_resource(SalesResource, '/sales')




# # Connecting from the server
# conn = mysql.connector.connect( host = '127.0.0.1',
#                                 user = 'root',
#                                 password ='root',
#                                 # database = 'ppcms_new_db'
#                                 database = 'ppcms_angthon'
#                               )
# if conn.is_connected():
#     print("successfull connected-------------")
# # preparing a cursor object
# cursorObject = conn.cursor()

# # query1 = "SELECT * FROM `account`"
# query1 = "SELECT * FROM `reg_cus_contact`"

# cursorObject.execute(query1)

# table=cursorObject.fetchall()
 
# print('\n Table Description:') 
# for attr in table:
#     print(attr)
#     print("--------------")

# cursorObject.close()

# # creating database
# # cursorObject.execute("SELECT * FROM `account`")

# # print(conn)
 
# # Disconnecting from the server
# conn.close()

# app = create_app()

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
    # app.run(host=appconfig.host, port=appconfig.host_port)
   

# -----------------------------------------------------------------------------

