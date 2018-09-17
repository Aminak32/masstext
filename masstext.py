#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import smtplib
import getpass
from progress.bar import Bar


def main(contacts, message):
    num_count = len(contacts)
    gmail_user = input("Gmail Username: ")
    gmail_password = getpass.getpass()
    subject = input("Subject: ")
    sent_from = gmail_user
    progress_bar = Bar("Sending...", max=num_count)

    with open("gateways.txt", "r") as gfile:
        gways = [l.strip() for l in gfile.readlines()]

    gateways = {l.split(',')[1]: l.split(',')[0] for l in gways}

    for (num, carrier) in contacts:
        try:
            with open("sent.txt", "r") as sent_file:
                if num in [a.strip() for a in sent_file.readlines()]:
                    print("Skipping: {}".format(num))
                    continue
        except IOError:
            pass
        print("Sending to {}...".format(num))
        gateway = gateways[carrier]
        recepient = num + "@" + gateway
        msg = 'From : {}\nTo: {}\nSubject: {}\n\n{}'.\
            format(gmail_user, recepient, subject, message)
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, recepient, msg)
            server.close()
            sent = True
        except BaseException:
            print("Failed to send!")
            sent = False
        if sent:
            with open("sent.txt", "a+") as sent_file:
                sent_file.write("{}\n".format(num))
            progress_bar.next()


if __name__ == "__main__":
    with open("contacts.txt", 'r') as cfile:
        CLINES = [l.strip() for l in cfile.readlines()]
        CONTACTS = [(l.split(',')[0], l.split(',')[1]) for l in CLINES]

    with open("message.txt", "r") as message_file:
        MESSAGE = message_file.read().replace('\n', '')
    main(CONTACTS, MESSAGE)
