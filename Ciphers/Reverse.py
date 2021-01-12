# Reverse cipher

message = 'daed era meht fo owt fi ,terces a peek nac eerhT'
translated = ''

i = len(message) - 1
while i >= 0:
    translated += message[i]
    i -= 1

print(translated)