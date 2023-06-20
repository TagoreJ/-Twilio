
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid ='AC28e870aa9479b10fea3699cc40c04441'
auth_token = 'bef67866c855430546f6a85f61294a83'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml="<Response><Say>      hello Indhu kuka         how are you bandi            nanka</Say></Response>" ,
                        to='+916303561878',
                        from_='+12058904813'
                    )

print(call.sid)      
      
