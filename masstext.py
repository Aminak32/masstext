import os
import smtplib
import getpass
from time import sleep
from progress.bar import Bar

def main():
    with open("gateways.txt", "r") as f:
        gateways = f.readlines()

    with open("numbers.txt", "r") as f:
        num_count = len(f.readlines())

    gmail_user = input("Gmail Username: ")
    gmail_password = getpass.getpass()
    sent_from = gmail_user
    subject = input("Please enter a subject: ")
    bar = Bar("Sending...", max=num_count)

    with open("message.txt", "r") as message_file:
        message = message_file.read().replace('\n', '')

    with open("numbers.txt", "r") as numbers:
        for num in [n.strip() for n in numbers.readlines()]:
            with open("sent.txt", "r") as f:
                if num in [a.strip() for a in f.readlines()]:
                    print("Skipping: {}".format(num))
                    continue
            print("Sending to {}".format(num))
            for gateway in gateways:
                to = num + "@" + gateway
                msg = 'From : {}\nTo: {}\nSubject: {}\n\n{}'.\
                    format(gmail_user, to, subject, message)
                try:
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.ehlo()
                    server.login(gmail_user, gmail_password)
                    server.sendmail(sent_from, to, msg)
                    server.close()
                    sent = True
                except:
                    print('Something went wrong...')
                    sent = False
                if sent:
                    with open("sent.txt", "a") as sent_file:
                        sent_file.write("{}\n".format(num))

if __name__ == "__main__":
    main()
