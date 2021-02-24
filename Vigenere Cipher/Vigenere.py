def generateKey(string,key):
    key = list(key) 
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i % len(key)])
    return("" . join(key)) 
	

def Encrypt(string, key):
    cipher_text = [] 
    for i in range(len(string)): 
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    cipher= ("" . join(cipher_text))
    print("Ciphertext : ", cipher)
	

def Decrypt(cipher_text, key):
    orig_text = [] 
    for i in range(len(cipher_text)):
        x = ((ord(cipher_text[i]) - ord(key[i]) + 26) % 26)
        x += ord('A')
        orig_text.append(chr(x)) 
    original= ("" . join(orig_text))
    print("Decrypted Text : ", original)
	

def main():
    plain = str(input("Enter string: "))
    string= plain.upper()
    token = str(input("Enter key: "))
    keyword=token.upper()
    key = generateKey(string, keyword)
    choice=int(input("Do you want to 1. Encrypt or 2. Decrypt the message? (1/2) "))
    if choice==1:
        Encrypt(string,key)
    elif choice==2:
        Decrypt(string, key)
    else:
        pass
    	 

if __name__ == '__main__':
    main()
