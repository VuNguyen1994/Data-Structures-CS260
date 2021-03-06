# Name: Dinh Nguyen, CS260 Summer 2020

import bcrypt
import time

# dln45,$2b$12$vJyztxDc3KyOZRGGqIQMIO5zOEPvGlcsIj7joMZpkFBkc81rhv1c2
# dms569,$2b$12$iGyvhQc.WXiLywZdA4cDyOR9jzT.A3E3WXdO.r6Uow4JMQ7xqZMHy
# dpn34,$2b$12$/PPfmTgM9zhy3EPNoLgbrudnnz/27.wi.OjwVlmry4FrMsJuYJUv2

def char_init(alphabet):
    # init a list of character from a-z
    ch = 'a'
    for i in range(0,26):
        alphabet.append(ch)
        ch = chr(ord(ch)+1)
    return alphabet

def find_pw(digest1,digest2,digest3):
    pw_found = 0
    count = 0
    start = time.time()
    for i in range(0,26):
        for k in range(0,26):
            passwd = alphabet[i] + alphabet[k]
            passwd = passwd.encode()
            count +=1
            if bcrypt.checkpw(passwd,digest1): # match password of dln45
                print("Password dln45  : %s , Number of guesses: %d, Time: %f mins" % ( passwd.decode(), count, (time.time()-start)/60 ))
                pw_found +=1
            if bcrypt.checkpw(passwd,digest2): # match password of dms569
                print("Password dms569 : %s , Number of guesses: %d, Time: %f mins" % ( passwd.decode(), count, (time.time()-start)/60 ))
                pw_found +=1
            if bcrypt.checkpw(passwd,digest3): # match password of dpn34
                print("Password dpn34  : %s , Number of guesses: %d, Time: %f mins" % ( passwd.decode(), count, (time.time()-start)/60 ))
                pw_found +=1
            if pw_found == 3:
                return

if __name__ == '__main__':
    digest1 = b'$2b$12$vJyztxDc3KyOZRGGqIQMIO5zOEPvGlcsIj7joMZpkFBkc81rhv1c2'    # dln45
    digest2 = b'$2b$12$iGyvhQc.WXiLywZdA4cDyOR9jzT.A3E3WXdO.r6Uow4JMQ7xqZMHy'    # dms569 
    digest3 = b'$2b$12$/PPfmTgM9zhy3EPNoLgbrudnnz/27.wi.OjwVlmry4FrMsJuYJUv2'    # dpn34
    alphabet = []
    char_init(alphabet)
    print("Searching for passwords......")
    find_pw(digest1, digest2, digest3)
         