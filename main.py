import Publickey

message = ''' Hello world!
strig= 'j1iCTEn34LcZgneeRVcQIaS2YnxBDEUBWhTeaVcTufTPHuJjr5GZcYp4WQUP5bhTEwiEIC5RbcffhCEh2J4c5jbolaI7XNkSYDhFK'
 '''
key = Publickey.generateKey(1024)
print(key)
C = Publickey.encryption(key[0],message)
print(C)
M = Publickey.decryption(key[1],C)

