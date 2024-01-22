import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["Subject"]= "This is a trial email"
email["To"]= "vaishaliranjan2@gmail.com"
email["From"]= "vaishaliranjan3@gmail.com"
email_content= '''
Dear Sir/Ma'am,
This is a trial email.

Regards
Vaishali Ranjan
'''

email.set_content(email_content)
smtp_connector=smtplib.SMTP(host="smtp.gmail.com", port=587)
smtp_connector.starttls()
smtp_connector.login("vaishaliranjan3@gmail.com", "Vaishali@12345")
smtp_connector.send_message(email)