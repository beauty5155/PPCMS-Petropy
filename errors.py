# 200 - Success no display in the front end
# 300 - Display as /warning in form
# 400 - Display in Alert/Popup

DEFAULT_REFID='EXCEPTION'

TYPE_EXCEPTION='EXCEPTION'
TYPE_EXPIRED='EXPIRED'

custom_errors = {
    "SUCCESS": {
        "refid": 0,
        "status_code": 200,
        "ec": 200,
        "message": "Success"
    },
    "FAILED": {
        "status_code": 400,
        "ec": 300,
        "message": "Request Failed"
    },
    # "TOKEN_ERROR": {
    #     "status_code": 400,
    #     "ec": 301,
    #     "message": ""
    # },
    # "TOKEN_EXPIRED": {
    #     "status_code": 400,
    #     "ec": 302,
    #     "message": "Connection Timed Out"
    # },
    # "INVALID_APP_KEY": {
    #     "status_code": 400,
    #     "ec": 303,
    #     "message": "Invalid App Key"
    # },
    "GENERAL_ERROR": {
        "refid": 0,
        "status_code": 400,
        "ec": 401,
        "message": "General Error"
    },
    "API_ERROR": {
        "refid": 0,
        "status_code": 400,
        "ec": 402,
        "message": "API Error"
    },
    "REG_CUS_CONTACT_ALREADY_EXIST": {
        "refid": 0,
        "status_code": 300,
        "ec": 501,
        "message": "Customer already registered"
    },
    "CUSTOMER_NOT_FOUND": {
        "refid": 0,
        "status_code": 300,
        "ec": 502,
        "message": "Customer not found"
    },
    "USER_NOT_FOUND": {
        "status_code": 300,
        "ec": 1001,
        "message": "Customer does not exist, please register"
    },
    "INCORRECT_PASSWORD": {
        "status_code": 300,
        "ec": 1002,
        "message": "Incorrect Password, please enter correct password"
    },


}