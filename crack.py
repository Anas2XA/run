from hashlib import md5

flag = 0
pass_hash = input ("Enter md5 hash: ")

wordlist = input("File name: ")
try: 
    pass_file = open (wordlist, "r") 
except:
    print("No file found")    
    quit()
    
for word in pass_file:
    enc_wrd = word.encode('utf-8')
    digest = md5(enc_wrd.strip()).hexdigest()

    if digest ==pass_hash:
        print("Password found")
        print("Password is " + word)
        flag = 1
        break
if flag ==0:
    print("password/passphrase is not in the list" )