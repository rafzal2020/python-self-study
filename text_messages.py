#Importing the twilio client to allow the code to work
from twilio.rest import Client

#Inserting the account numbers given to me to authorize my account it the code.
account_sid  = "account_sid"
auth_token = "auth_token"
client = Client(account_sid, auth_token)

#Creating a message that will be sent to my phone number from a given phone number with a custom message.
client.messages.create(to = "personal number",
	from_="twiliophonenumber",
	body = "Hello!")
