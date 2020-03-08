#Name:Anup Joseph
#Roll No:8351
#Batch: C
import string
import math 

def message_builder(m):
    return [ ord(i) - 96 if i>= 'a' else ord(i) - 64 for i in m ]

def key_builder(key_text,factor):
    key = []
    for i in range(factor):
        for j in range(len(key_text)):
            key.append(key_text[j])
    key = key[:len(plain_text)]
    return key

def vernam_maker(plain_text,key_text):
    #Key Building
    factor = len(plain_text)//len(key_text) + 1
    key = key_builder(key_text,factor)
    #Verman Encoding
    cypher_text = [ plain_text[i] + key[i] for i in range(len(plain_text)) ]
    cypher_text = [ cypher_text[i] - 26 if cypher_text[i]>26 else cypher_text[i] for i in range(len(cypher_text))]
    cypher_text = [ cypher_text[i] - 1 for i in range(len(cypher_text)) ]
    cypher_text = [chr(ord('@')+i) for i in cypher_text]
    print("Message after vernam encoding {}".format(cypher_text))
    return cypher_text

#Decryption of Vernam cypher
def vernam_decrypt(cypher_text,key):
    factor = len(cypher_text)//len(key) + 1
    key = key_builder(key,factor)
    print(key)
    plain_text = [cypher_text[i]-key[i] for i in range(len(cypher_text))]
    plain_text = [plain_text[i] + 26 if plain_text[i]<0 else plain_text[i] for i in range(len(plain_text))]
    plain_text = [chr(ord('@')+i+1) for i in plain_text]
    print("Message after vernam encoding {}".format(plain_text))
    return plain_text

# Encryption
def encryptMessage(msg,key): 
	cipher = "" 
	# track key indices 
	k_indx = 0
	msg_len = float(len(msg)) 
	msg_lst = list(msg) 
	key_lst = sorted(list(key)) 
	# calculate column of the matrix 
	col = len(key) 
	# calculate maximum row of the matrix 
	row = int(math.ceil(msg_len / col)) 

	# add the padding character '_' in empty 
	# the empty cell of the matix 
	fill_null = int((row * col) - msg_len) 
	msg_lst.extend('_' * fill_null) 

	# create Matrix and insert message and 
	# padding characters row-wise 
	matrix = [msg_lst[i: i + col] 
			for i in range(0, len(msg_lst), col)] 

	# read matrix column-wise using key 
	for _ in range(col): 
		curr_idx = key.index(key_lst[k_indx]) 
		cipher += ''.join([row[curr_idx] 
						for row in matrix]) 
		k_indx += 1

	return cipher 

# Decryption 
def decryptMessage(cipher): 
	msg = "" 

	# track key indices 
	k_indx = 0

	# track msg indices 
	msg_indx = 0
	msg_len = float(len(cipher)) 
	msg_lst = list(cipher) 

	# calculate column of the matrix 
	col = len(key) 
	
	# calculate maximum row of the matrix 
	row = int(math.ceil(msg_len / col)) 

	# convert key into list and sort 
	# alphabetically so we can access 
	# each character by its alphabetical position. 
	key_lst = sorted(list(key)) 

	# create an empty matrix to 
	# store deciphered message 
	dec_cipher = [] 
	for _ in range(row): 
		dec_cipher += [[None] * col] 

	# Arrange the matrix column wise according 
	# to permutation order by adding into new matrix 
	for _ in range(col): 
		curr_idx = key.index(key_lst[k_indx]) 

		for j in range(row): 
			dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
			msg_indx += 1
		k_indx += 1
	# convert decrypted msg matrix into a string 
	try: 
		msg = ''.join(sum(dec_cipher, [])) 
	except TypeError: 
		raise TypeError("This program cannot handle repeating words.") 
	null_count = msg.count('_') 
	if null_count > 0: 
		return msg[: -null_count] 
	return msg 


plain = input("Enter plain text")
key = input("Enter key text")
plain_text = message_builder(plain) 
key_text = message_builder(key)

cypher_text = vernam_maker(plain_text,key_text)

cipher = encryptMessage(cypher_text,key) 
print("Encrypted Message after processing through single cloumnar transposition using the same key: {}".format(cipher)) 
cipher = decryptMessage(cipher)
print("Decryped Message: {}".format(cipher)) 

cipher = message_builder(cipher)
final_output = vernam_decrypt(cipher,key_text)

#Output
# Enter plain textHOWAREYOU
# Enter key textncbtzqarx
# Message after vernam encoding ['U', 'Q', 'X', 'T', 'Q', 'U', 'Y', 'F', 'R']
# Encrypted Message after processing through single cloumnar transposition using the same key: YXQUUFTRQ
# Decryped Message: UQXTQUYFR
# [14, 3, 2, 20, 26, 17, 1, 18, 24]
# Message after vernam encoding ['H', 'O', 'W', 'A', 'R', 'E', 'Y', 'O', 'U']