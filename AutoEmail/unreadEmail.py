import ezgmail

#Checks work email for unread emails

unreadThreads = ezgmail.unread()

ezgmail.summary(unreadThreads)

# Reads number of unread threads
print('You have ' + str(len(unreadThreads)) + ' unread thread(s) in your work email')

# Prints first unread email with all contents
print(str(unreadThreads[0].messages[0]))

# Prints subject of first unread email
print(unreadThreads[0].messages[0].subject)

# Prints body of first unread email
print(unreadThreads[0].messages[0].body)

print(unreadThreads[0].messages[0].timestamp)

print(unreadThreads[0].messages[0].sender)

print(unreadThreads[0].messages[0].recipient)
ezgmail.send('glenlarkin@gmail.com', 'You have ' + str(len(unreadThreads)) + ' unread thread(s) in your work email', 'Please read your unread threads from ' + unreadThreads[0].messages[0].sender)