import smtplib

my_email = "matikomaroa10@gmail.com"
yahoo_email = "ndoniwilliam09@gmail.com"
password = "#######"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=yahoo_email,
                        msg="Subject:Hello\n\nboom boom")
