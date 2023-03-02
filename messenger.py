from twilio.rest import Client


class Messenger:
    TWILIO_ACCOUNT_SID = 'AC4d9c9e66bcbffc1f85019a23ab68ec1f'
    TWILIO_AUTH_TOKEN = '9b816156b4a0c01275edb217abb18211'
    TWILIO_PHONE_NUMBER = '+18445700369'
    DESTINATION_PHONE_NUMBER = '+13463397625'
    client = 0

    def __init__(self):
        # Initialize client as Twilio account
        self.client = Client(self.TWILIO_ACCOUNT_SID, self.TWILIO_AUTH_TOKEN)

    def sendMessage(self, message):
        self.client.messages.create(
            body=message,
            from_=self.TWILIO_PHONE_NUMBER,
            to=self.DESTINATION_PHONE_NUMBER
        )
        print('TWILIO :: Notification sent!')
