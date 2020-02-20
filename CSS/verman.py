plain_text = [ ord(i) - 96 if i>= 'a' else ord(i) - 64 for i in input("Enter plain text") ] 
key_text = [ ord(i) - 96 if i>= 'a' else ord(i) - 64 for i in input("Enter plain text") ]

#Key Building
factor = len(plain_text)//len(key_text) + 1
key = []
for i in range(factor):
    for j in range(len(key_text)):
        key.append(key_text[j])
key = key[:len(plain_text)]

#Verman Encoding
cypher_text = [ plain_text[i] + key[i] for i in range(len(plain_text)) ]
cypher_text = [ cypher_text[i] - 26 if cypher_text[i]>26 else cypher_text[i] for i in range(len(cypher_text))]
cypher_text = [ cypher_text[i] - 1 for i in range(len(cypher_text)) ]
print("Message after vernam encoding {}".format(cypher_text))

tempkey = sorted(key)
