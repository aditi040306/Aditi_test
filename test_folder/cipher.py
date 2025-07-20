def encrypt(str,N,D):
    print("Encrypting with N:", N, "D:", D, "String:", str)
    # Placeholder for encryption logic
    if '!' in str or ' ' in str:
        print("Invalid characters in string for encryption")
        return None
    else:
        str=str[::-1]
        print("Reverse string:", str)
        ascii_values = [ord(char) for char in str]
        print(f"The ASCII values of '{str}' are: {ascii_values}")
        
        if N >= 1  and D == 1 :
            for i in range(len(ascii_values)):
                ascii_values[i] = (ascii_values[i] + N) % 256
            print(f"The encrypted ASCII values are: {ascii_values}")
            encrypted_str = ''.join(chr(value) for value in ascii_values)
            print(f"The encrypted string is: {encrypted_str}")
            return encrypted_str
         
        elif N >= 1  and D == -1 :
            for i in range(len(ascii_values)):
                ascii_values[i] = (ascii_values[i] - N) % 256
            print(f"The encrypted ASCII values are: {ascii_values}")
            encrypted_str = ''.join(chr(value) for value in ascii_values)
            print(f"The encrypted string is: {encrypted_str}")
            return encrypted_str
            
        else:
            print("Invalid N or D values for encryption")
            return None
    
 

def decrypt(str,N,D):
    print("Decrypting with N:", N, "D:", D, "String:", str)
    # Placeholder for encryption logic
    if '!' in str or ' ' in str:
        print("Invalid characters in string for encryption")
        return None
    else:
        #str=str[::-1]
        #print("Reverse string:", str)
        ascii_values = [ord(char) for char in str]
        print(f"The ASCII values of '{str}' are: {ascii_values}")
        
        if N >= 1  and D == 1 :
            for i in range(len(ascii_values)):
                ascii_values[i] = (ascii_values[i] - N) % 256
            print(f"The dencrypted ASCII values are: {ascii_values}")
            dencrypted_str = ''.join(chr(value) for value in ascii_values)
            print(f"The dencrypted string is: {dencrypted_str}")
            dencrypted_str=dencrypted_str[::-1]
            print("Reverse string:", dencrypted_str)
            if '!' in dencrypted_str or ' ' in dencrypted_str:
                print("Invalid characters in string for encryption")
                return None
            else:
                return dencrypted_str
         
        elif N >= 1  and D == -1 :
            for i in range(len(ascii_values)):
                ascii_values[i] = (ascii_values[i] + N) % 256
            print(f"The dencrypted ASCII values are: {ascii_values}")
            dencrypted_str = ''.join(chr(value) for value in ascii_values)
            print(f"The dencrypted string is: {dencrypted_str}")
            dencrypted_str=dencrypted_str[::-1]
            print("Reverse string:", dencrypted_str)
            if '!' in dencrypted_str or ' ' in dencrypted_str:
                print("Invalid characters in string for encryption")
                return None
            else:
                return dencrypted_str
        
        
            
        else:
            print("Invalid N or D values for encryption")
            return None
 

encrypt ("TEST",2,1)
decrypt ("VUGV",2,1)