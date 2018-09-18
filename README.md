# masstext
> A python module for sending a mass text message using SMS gateways

## Description

Given a list of phone numbers and their carriers, masstext lets you use
your gmail account to send a text to each phone number using its carrier's sms
gateway.

## Getting Started

To use masstext, two txt files must be created in the ```data``` directory

1. contacts.txt - A file containing values of the form x,y on every line, where x
                  is a phone number and y is its carrier.

2. message.txt - A file containing the actual message to be sent

Examples of both of these files can be found in the data directory

## Carriers

A carrier must be one of the following: VMOBILE, VERIZON, TMOBILE, SPRINT, METROPCS, BOOSTMOBILE, ATT. 
To add a carrier, append a string of the form x,y to ```data/gateways.txt``` where x is a carrier and y is its SMS gateway. 

## Example Usage

Once you've created ```data/contacts.txt``` and ```data/message.txt```, simply
run ```masstext.py``` to send the email. It will prompt you for your gmail
credentials along with a subject for the text.
```
    $ python masstext.py
    Gmail Username: test@gmail.com
    Password: 
    Subject: This is a test
    Sending to 3141592653...
    Sending to 2718281828...
```
