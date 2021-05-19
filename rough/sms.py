import smtplib
from urllib import request
from http import cookiejar as cookielib
# from stat import *
from textmagic.rest import TextmagicRestClient
from twilio.rest import Client

def send_sms(data):
    message = data
    number = "9620115502" #to which number sms should be sent

    if __name__ == "__main__":
        username = ""  # ""
        passwd = "A3969Q"        # "Q9639K"

        message = "+".join(message.split(' '))

    #logging into the sms site
        url ='http://site24.way2sms.com/Login1.action?'
        data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

    #For cookies

        cj= cookielib.CookieJar()
        opener = request.build_opener(request.HTTPCookieProcessor(cj))

    #Adding header details
        opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
        try:
            usock =opener.open(url, data.encode("utf-8"))
        except IOError:
            print ("error")
            #return()

        jession_id =str(cj).split('~')[1].split(' ')[0]
        send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
        send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
        opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
        try:
            sms_sent_page = opener.open(send_sms_url,send_sms_data.encode("utf-8"))
        except IOError:
            print ("error")

        print("success")

def send_sms2(message):
    username = "your_textmagic_username"
    token = "your_apiv2_key"
    client = TextmagicRestClient(username, token)

    message = client.messages.create(phones="", text=message)

def send_sms3(message):
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=message,
                         from_='+',
                         to='+'
                     )

    print(message.sid)



send_sms3("Testing")
