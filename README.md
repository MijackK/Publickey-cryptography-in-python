# MyRSAimplementation
An  implementation of RSA using ECB blocking, implementation uses 50 characters per block for a 1024 bit key, block size can increase with an increase in key size.


<h1>Example of running the program:</h1>
message='hello world'<br>
key = generateKey(1024)<br>
C=encryption(key[0],message)<br>
M=decryption(key[1],C)<br>
print(M)<br>
