import random, primeNum, cryptoMath, rsainteger


def generateKey(keySize):
    p = 0
    q = 0
    while p == q:
        p = primeNum.generateLargePrime()
        q = primeNum.generateLargePrime()
    n = p * q
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** keySize)
        if cryptoMath.gcd(e, (p - 1) * (q - 1)) == 1:
            break
    d = cryptoMath.findModInverse(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)

    return publicKey, privateKey


def encryption(public, plainText):
    encryptedMessage = rsainteger.makeBlock(plainText)
    numberofblocks = len(encryptedMessage)
    cipherIntegers = [0] * numberofblocks
    for x in range(numberofblocks):
        cipherIntegers[x] = pow(encryptedMessage[x], public[1], public[0])
    return cipherIntegers


def decryption(private, cipherMessage):
    for x in range(len(cipherMessage)):
        cipherMessage[x] = pow(cipherMessage[x], private[1], private[0])
    plainText = rsainteger.blockTotext(cipherMessage)
    return plainText


