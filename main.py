import smtplib
import random
import datetime as dt



with open("quotes.txt") as file:
    data = file.readlines()

now = dt.datetime.now()
dat = now.date()
wekk = dat.weekday()

if wekk == 6:
    qout = random.choice(data)
    print(qout)
    my_email = "yashu143darling11@gmail.com"
    password = "iytevtpyixfnfwuw"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="yashudarlingtest@yahoo.com", msg=qout)
    connection.close()
