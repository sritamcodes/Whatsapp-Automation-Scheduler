#Step1: Install the Twilio library using pip
from twilio.rest import Client
from datetime import datetime,timedelta
import time
#Twilio Credentials
account_sid="YOUR_TWILIO_ACCOUNT_SID"
auth_token='YOUR_TWILIO_AUTH_TOKEN'

client=Client(account_sid,auth_token)
#Step3: Define the message and recipient
def send_whatsapp_message(recipient_number,message_body):
    try:
        message=client.messages.create(
            from_='whatsapp:YOUR_TWILIO_WHATSAPP_NUMBER',
            body=message_body,
            to=f"whatsapp:{recipient_number}"
        )
        print(f"Message sent to {recipient_number}: {message.sid}")
    except Exception as e:
        print(f"Failed to send message to {recipient_number}: {str(e)}")
#Step4: Schedule the message to be sent at a specific time
name=input("Enter the name of the recipient: ")
recipient_number=input("Enter the recipient's WhatsApp number (with country code): ")
message_body=input("Enter the message you want to send: ")
#step5: Get the current time and calculate the delay until the scheduled time
date_str=input("Enter the date and time to send the message (YYYY-MM-DD HH:MM:SS): ")
time_str=input("Enter the time to send the message (HH:MM): ")

#datetime
scheduled_time=datetime.strptime(date_str+" "+time_str, "%Y-%m-%d")
current_time=datetime.now()
#calculate the delay
time_difference=(scheduled_time-current_time)
delay_seconds=time_difference.total_seconds()
if delay_seconds<=0:
    print("Scheduled time must be in the future.")
else:
    print(f"Message will be sent to {recipient_number} at {scheduled_time}.")
#Step6: Wait until the scheduled time and send the message
time.sleep(delay_seconds)
#send the message
send_whatsapp_message(recipient_number,message_body)

