from lxml import html
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# gsu, gtech, oregon, uiuc,uic, purdue, cornell
pages = ['https://www.thegradcafe.com/survey/index.php?q=georgia+state+university*+computer+science*&t=n&o=','https://www.thegradcafe.com/survey/index.php?q=georgia+institute+of+technology*+computer+science*&t=n&o=','https://www.thegradcafe.com/survey/index.php?q=oregon+state+university*+computer+science*&t=n&o=','https://www.thegradcafe.com/survey/index.php?q=university+of+illinois+urbana*+computer+science*&t=n&o=', 'https://www.thegradcafe.com/survey/index.php?q=university+of+illinois+chicago*+computer+science*&t=n&o=','https://www.thegradcafe.com/survey/index.php?q=purdue*+computer+science*&t=n&o=','https://www.thegradcafe.com/survey/index.php?q=cornell*+computer+science*&t=n&o=']

sender_email = 'sender-email-id'
send_password = 'sender-password'
reciever_email = 'reciever-email-id'

lastcontent = ['' for i in range(len(pages))]

universities = []
program = []
status = []
date = []
notes = []

def crawler():
    universities = []
    program = []
    status = []
    date = []
    notes = []
    print(lastcontent)
    for i, page in enumerate(pages):
        page = requests.get(page)
        tree = html.fromstring(page.content)
        rows = tree.xpath('//tr')

        if(len(rows) > 1):
            for row in rows[1:]:
                if(lastcontent[i] == row.text_content()):
                    print('yo')
                    continue
                universities.append(row[0].text_content())
                program.append(row[1].text_content())
                status.append(row[2].text_content())
                date.append(row[4].text_content())
                if(len(row) == 6):
                    notes.append(row[5].text_content())
                
                lastcontent[i] = row.text_content()
    
    print(universities, program, status, date, notes)


def send_mail():
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(sender_email,send_password) 

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Alert from ' + str(universities)[1:-1]
    msg['From'] = sender_email
    msg['To'] = reciever_email

    body = 'There are status updates in the following universities: \n'

    for i,_ in enumerate(universities):
        body += universities[i] + '  ' + program[i] + '  ' + status[i] + '  ' + date[i] + '  ' + notes[i] + '\n'

    part1 = MIMEText(body, 'plain')
    msg.attach(part1)

    s.sendmail(sender_email, reciever_email, msg.as_string()) 
    s.quit()


while(1):
    crawler()
    if(len(universities) > 0):
        send_mail()
    time.sleep(60*60)
