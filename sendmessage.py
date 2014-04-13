import smtplib, time
from amahelp import *
from users import *
from emailChecker import *

def setup():
        server = smtplib.SMTP()
	server.connect("smtp.gmail.com", "587")
	server.ehlo()
        server.starttls()
        server.login('amahelper@gmail.com', 'hackIllinois')
	return server
def init_users():
	theEmails = getEmailData()

	theusers = Users()

	for i in theEmails:
		userinfo = parseEmailData(theEmails[i])
		theusers.buildUser(userinfo[0] + "|" + userinfo[1] + "~" + "300")
		
	
	return theusers

def clear_file():
	f = open("user_info.txt","w").close()
def send_top_ama():
	server = setup()
	theusers = init_users()
	print theusers.myusers[0].provider
	submissions = login()
	for x in submissions:
	#	theusers.refresh()
		for user in theusers.myusers:
			if x.ups <= user.quality:
				recipient = str(user.number) + str(user.provider)
				#print recipient
				server.sendmail("amahelper@gmail.com", recipient, str(x)) #AND LINK
	server.quit()

def main():
	clear_file()
	while(True):
		a = int(time.strftime("%M"))
		if a%10 == 0: #change for demo

			send_top_ama()	
		
			time.sleep(600)

main()
