import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "esamuratovf@gmail.com"
receiver_email = "absaitovdev@gmail.com"
password = "zmybyocirtvtajos"
message = """\
Subject: 
    https://github.com/davron754/exam-4
"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
