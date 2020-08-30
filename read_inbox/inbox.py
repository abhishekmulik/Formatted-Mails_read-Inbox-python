import imaplib
import email
import credentials

host='imap.gmail.com'
username=credentials.username
password=credentials.password

mail=imaplib.IMAP4_SSL(host)
mail.login(username,password)
mail.select('inbox')
_, search_data=mail.search(None,'UNSEEN')  ##UNSEEN for unssen msgs and SEEn for seen msgs
#print(search_data)

for num in search_data[0].split():
    _, data=mail.fetch(num,'(RFC822)')
    _,b=data[0]
    email_meassage=email.message_from_bytes(b)
    
    for header in ['From','Subject','To','Date']:
        print("{}: {}".format(header,email_meassage[header]))
        
    for part in email_meassage.walk():
        if part.get_content_type()=='text/plain' or part. get_content_type()=='text/html':
            body=part.get_payload(decode=True)
            print(body.decode())