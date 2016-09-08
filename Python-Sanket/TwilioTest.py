from twilio.rest import TwilioRestClient

account_sid = "AC97f5cbd3431862da84094e8e8b3806b0" # Your Account SID from www.twilio.com/console
auth_token  = "7f8681a677babcfdf2052d594f4cd376"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Sanket (Python)",
    to="+918097351816",    # Replace with your phone number
    from_="+12055888296") # Replace with your Twilio number

print(message.sid)