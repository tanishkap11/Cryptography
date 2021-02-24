def Encrypt(text,shift): 
    Etext = "" 
  
    for i in range(len(text)): 
        ch = text[i]

        if (ch == " "):
            Etext += " "
            i+=1
  
        elif (ch.isupper()): 
            Etext += chr((ord(ch) + shift - 65) % 26 + 65) 
  
        else: 
            Etext += chr((ord(ch) + shift - 97) % 26 + 97) 
  
    print("Encrypted Message : "+Etext)

def Decrypt(text,shift): 
    Dtext = "" 
  
    for i in range(len(text)): 
        ch = text[i]

        if (ch == " "):
            Dtext += " "
            i+=1
      
        elif (ch.isupper()): 
            Dtext += chr((ord(ch) - shift - 65) % 26 + 65) 
  
        else: 
            Dtext += chr((ord(ch) - shift - 97) % 26 + 97) 
  
    print("Decrypted Message :  "+Dtext)
  
def main():
    text = str(input("Enter Message : "))
    shift = int(input ("Enter key : "))
    choice=int(input("Do you want to 1. Encrypt or 2. Decrypt the message? (1/2) "))
    if choice==1:
        Encrypt(text,shift)
    elif choice==2:
        Decrypt(text, shift)
    else:
        pass

if __name__ == '__main__':
    main()
