#!python3
# Pings each server to see if they are online

import os, csv

with open('SysAdmin/apwServers.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # Convert Server IPs to list
    newList = list(reader)
    output = ''

    # Loop through CSV List
    for row in newList:
        ipAddr = row[0]

        # Ping each server
        response = os.system('ping -c 2 ' + ipAddr)
        if response == 0:
            output += ipAddr + ' is up :)\n'
        else:
            output += ipAddr + ', is down :(\n'

print(output + 'have a nice day')