from formatting import format_msg
import requests
from datetime import datetime
import sys
from sendMail import send_mail

def send(name,website=None,to_emails=None,verbose=False):
    assert to_emails != None
    if website != None:
        msg=format_msg(my_name=name,my_website=website)
    else:
        msg=format_msg(my_name=name)
    if verbose:
        print(name,website,to_emails)
    #send the msg
    try:
        send_mail(text=msg,to_emails=[to_emails],html=None)
        sent=True  
    except:
        sent=False
    return sent

if __name__ == "__main__":
    #print(sys.argv)
    if len(sys.argv)>1:
        name=sys.argv[1]    ###sys.argv return list of arguments (try printing it).
    email= None
    if len(sys.argv)>2:
        email=sys.argv[2]
    response=send(name,to_emails=email,verbose=True)
    print(response)
