#!/usr/bin/python3

# Checks repositories for updates, lists updates, then run update if desired
import os

print('Checking for Updates to run')

sudo_password = 'fuck0ff'

command = 'apt-get update'
os.system('echo %s|sudo -S %s' % (sudo_password, command))

command = 'apt list --upgradeable'
updates = os.system(command)

if updates == 0:
    print('No updates to run')

else:
    print("Updates are available \n" + updates )

    question = input("Would you like to update? ")
    if question == 'y' or question == 'yes':
        
        command = 'apt-get upgrade -y'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))
    else:
        print("Update Canceled")

# TODO implement update logging

# State time update was run
# State what apps were updated