from Crypto.Cipher import AES
from Crypto import Random
import base64

def Encrypt(text):
    size = 16 
    func_padding = lambda text : text+(size-len(text)%size)*"*"
    KEY = Random.new().read(16)
    IV = Random.new().read(16)
    args = AES.new(KEY,AES.MODE_CBC,IV) 
    encrypted = IV + args.encrypt( func_padding(text).encode('utf-8'))
    encoded = base64.b64encode(encrypted)
    return [KEY,encoded]

def Decrypt(KEY,encrypted):
    decoded = base64.b64decode(encrypted)[16:]
    IV_ = base64.b64decode(encrypted)[:16]
    args_ = AES.new(KEY,AES.MODE_CBC,IV_)
    decrypted = args_.decrypt(decoded).decode('utf-8')
    return decrypted.rstrip("*")

while True:
    ch =int(input("Press 1 to encrypt || Press 2 to decrypt\n>>>"))
    if ch == 1:
        data = Encrypt(input("Text:"))
        print("===================================================")
        print("                  !! Encrypted !!                  ")
        print(data[1])
        print("===================================================\n")
    elif ch == 2:
        KEY = data[0]
        encrypted = data[1]
        print("====================================================")
        print("                   !! Decrypted !!                  ")
        print(Decrypt(KEY,encrypted))
        print("====================================================\n")
