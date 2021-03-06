import imaplib
import email


def getEmailData():
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login('amahelper@gmail.com', 'hackIllinois')
	mail.list()
	mail.select('inbox')
	result, data = mail.search(None, 'ALL')
	if result != 'OK':
		print "No messages"

	ids = data[0]
	theEmails = {}	
	for i in ids.split():

		result, data = mail.fetch(i, "(RFC822)")
		raw_email = data[0][1]
		message = email.message_from_string(raw_email)

		##store in key
		for part in message.walk():
			if part.get_content_type() == 'text/plain':
				##store in value
				theEmails[i] = [message['From'], part.get_payload()]

	return theEmails

def parseEmailData(lista):
	theNum = lista[0]
	theNewNum = ""
	toReturn = []
	listofnums = ["0","1","2","3","4","5","6","7","8","9"]
	for i in theNum[: 15]:
		if i in listofnums:
			theNewNum += i
	toReturn.append(theNewNum)
	theString = lista[1]
	theString = theString[:theString.find("\n")]
	toReturn.append(theString)
	return toReturn
