import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

reply1 = str(input("would you like to said an email[y/n]: "))
if reply1 == "yes" or reply1 == "Yes" or reply1 == "Y" or reply1 == "y":
    mail_sender = str(input("enter your mail: "))
    mail_reciever = str(input("enter your mail reciever: "))
    if len(mail_sender) and len(mail_reciever) != 0:
        mail_subject = str(input("enter the subject of the mail: "))
        mail_text = str(input("message text: "))
        message = Mail(
            from_email=mail_sender,
            to_emails=mail_reciever,
            subject=mail_subject,
            plain_text_content=mail_text
        )
        try:
            sender = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            sending = sender.send(message)
            print("sending succesfully..")
            print(sending.status_code)
        except Exception as e:
            print(e.message)
elif reply1 == "N" or reply1 == "No" or reply1 == "no" or reply1 == "NO":
    print("exiting..")
else:
    print("sorry invalid input!.. quiting.")