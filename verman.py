message = list(input("Enter text message"))
key = list(input("Enter key for cipher"))
key = [ ord(i) - 97 for i in key]

factor = len(message)//len(key)
remainder = len(message)%len(key)

temp = [message.append('x') for i in range(len(message)-remainder)]

print(message)
message = [ ord(i)-97 for i in message]

message_block= []
temp_message = []
j = 0
for i in message:
    if j < len(key):
        temp_message.append(i)
        j = j + 1
    elif j == len(key):
        j = 0
        message_block.append(temp_message)
        temp_message = []
        temp_message.append(i)

print(message_block)
'''

temp_cypher = [ key[i] + message[i] for i in range(len(key))]
cypher = [ i%26 for i in temp_cypher]

print(cypher)'''
