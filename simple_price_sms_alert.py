from twilio.rest import TwilioRestClient

account_sid = "ACc55db698849f6b3b1b2c87e8da66d81d" # Your Account SID from www.twilio.com/console
auth_token  = "559d2c06a2ab6861750b417f4abb6940"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+15512083809",    # Replace with your phone number
    from_="+16468462195") # Replace with your Twilio number

print(message.sid)