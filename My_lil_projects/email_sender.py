import smtplib


s = smtplib.SMTP('smtp.gmail.com', 587)


s.starttls()
print("init")

s.login("analyticsto2ai@gmail.com", "ana2ai0967_!")
print("logged in")

message = 'Subject: {}\n\n{}'.format("Sheduler stopped", "Scheduler stopped due to some error ! Try  to run it again")
print("sending",message)

s.sendmail("analyticsto2ai@gmail.com","zaidmohd466@gmail.com", message)
print("Message send")
s.quit()