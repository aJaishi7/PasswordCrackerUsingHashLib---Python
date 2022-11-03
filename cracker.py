# Know as md5 in py2.7. In py3 converted to hashlib
# Go through of the application
# 1. We will have list of words which we supposed as probable passwords
# 2. List of hashes (Input hash) actual passwords

import hashlib

flag = 0  # flag = 1 if passowrd is found else 0
# Input Hash
password_hash = input('Please Enter Hash: \t')
input_file = input('FileName: \t')

try:
    password_container = open(input_file, 'r')

except:
    print('No File Selected')
    quit()


for word in password_container:
    # convert word in to utf-8 encoding format
    encoded_word = word.encode('utf-8')
    # create digest i.e hexadecimal format of encoded word
    # strip to clear any whitespaces
    digest = hashlib.md5(encoded_word.strip()).hexdigest()

    if (digest == password_hash):
        print('Password Found')
        print('Your Password is: ', word)
        flag = 1
        break

if (flag == 0):
    print('No Such Password Found In The List')
