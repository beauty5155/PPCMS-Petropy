from errors import custom_errors 


"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Method for getting customError message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
def customError(errStr, refId, msg=""):
    ce_dict = custom_errors[errStr].copy()
    ce_dict['refid'] = refId
    if (msg != ''):
        ce_dict['message'] = ce_dict['message']+' - '+msg
    if (ce_dict['status_code'] != 200):
        dispText = '\n> > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >'
        dispText = dispText + '\n' + 'Error:   \n'
        dispText = dispText + '\n' + str(ce_dict['ec']) + ' ' + ce_dict['message'] + '\n'
        dispText = dispText + '> > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >\n'
        print(dispText)
    return ce_dict
