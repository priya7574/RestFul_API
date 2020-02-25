# Sending emails without attachments using Python.
# importing the required library.
import smtplib

# creates SMTP session
email = smtplib.SMTP('smtp.gmail.com', 587)

# TLS for security
email.starttls()

# authentication
# compiler gives an error for wrong credential.
email.login("priyabharti.impinge@gmail.com", "P@77492P")
# email.login("smtp.impinge@gmail.com", "Smtp@12345")

# message to be sent
message = "message_to_be_send"

# sending the mail
email.sendmail("priyabharti.impinge@gmail.com", "vishalsharma.impinge@gmail.com", message)

# terminating the session
email.quit()