import smtplib, email
from email.mime.text import MIMEText

class Messenger:

    def sendMessage(self, message, recipient):
        # Color codes for console
        white = "\033[38;5;252m"
        pink = "\033[38;5;5m"
        red = "\033[38;5;1m"
        orange = "\033[38;5;3m"
        green = "\033[38;5;150m"
        blue = "\033[38;5;4m"
        purple = "\033[38;5;20m"

        msg = MIMEText(message)
        msg['Subject'] = "You're Amazon PriceTracker Notification"
        msg['From'] = "s2cupitt@gmail.com"
        msg['To'] = recipient
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login("s2cupitt@gmail.com", "patchy dinghy storm heavily untoasted skype")
        smtp_server.sendmail("s2cupitt@gmail.com", recipient, msg.as_string())
        smtp_server.quit()
        print(orange + 'SMTP :: ' + white + 'Notification sent!')
