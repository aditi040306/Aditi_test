import cipher

def testHW3():

    with open('database.txt', 'r') as file:
        lines = file.readlines()
        userarr = []
        passarr = []
        for line in lines:
            parts = line.strip().split(' ')
            if len(parts)>=2:
                userid= parts[0]
                userarr.append(userid)
                password = parts[1]
                passarr.append(password)
        print(f"UserID: {userarr}, Password: {passarr}")
        testHW2(userarr, passarr)




def testHW2(userarr,passarr):

    for i in range(len(userarr)):
        text1=userarr[i]
        text2=passarr[i]

        s=3
        d=1
        #encrypteduserid=cipher.encrypt(text1, s, d)
        #encryptedpasswd=cipher.encrypt(text2, s, d)

        originaluserid=cipher.decrypt(text1, s, d)
        originalpasswd=cipher.decrypt(text2, s, d)
        print(f"Original UserID: {originaluserid}, Original Password: {originalpasswd}")

def main():
    print("Running HW3 tests......")
    
    testHW3()
    

main()
