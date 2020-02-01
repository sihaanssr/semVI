import pdb
messsage = [ord(i) - 96 if i >= 'a' else ord(i) - 64 for i in input("\nEnter the message to be encrypted\n") ]
key = [ord(i) - 96 if i >= 'a' else ord(i) - 64 for i in input("\nEnter the key \n") ]

if len(key) <= len(messsage):
    remainder = len(messsage) % len(key)
    temp = [messsage.append(0) for i in range(remainder) ]
    factor = len(messsage)//len(key) 
i,j = 0,len(key)
cypher = []
while i < len(messsage):
    temp = messsage[i:i+len(key)]
    cypher.append([ (temp[x]+key[x])%26 for x in range(len(key))])
    i = i + len(key)
    pdb.set_trace()
print(cypher)
