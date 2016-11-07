from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC44fcffdc78d5819e973b04a865491de3"
auth_token  = "8f7dff85aa0ee1c4b68efeee5e17aca8"
client = rest.TwilioRestClient(account_sid, auth_token) #here we are creating an object/instance of class TwilioRestClient
 
message = client.messages.create(body="My name is Ron B",
    to="",    # Replace with your phone number
    from_="+12039007693") # Replace with your Twilio number
print message.sid
