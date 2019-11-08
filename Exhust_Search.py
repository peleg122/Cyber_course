#!/usr/bin/python
import random
import sys

# Part1:

file = open(sys.argv[1], 'r')
text = file.readlines()
line1 = text[0][0:-1].upper()
line2 = text[1].upper()
numberOfChars = len(line2)


def exhaustive_search(plain_txt):
    counter = 0
    working_line = plain_txt
    number = 0
    if len(line2) != len(plain_txt):
        print("Wrong input...")
    elif numberOfChars <= 0:
        print "None,", counter
    elif numberOfChars > 0:
        while counter != 25:
            final_message = ""
            if counter == 0:
                print working_line + ",", counter
            for x in range(0, len(working_line)):
                if ord(working_line[x]) in range(65, 91):
                    final_message += (chr(((ord(working_line[x])-64) % 26)+65))
            counter = counter + 1
            working_line = final_message
            if line2 == final_message:
                number = counter
            print working_line+",", counter
        if number == 0:
            print "No Solution"
        else:
            print number
        return number


exhaustive_search(line1)

# Part 2:

file2 = open(sys.argv[2], 'r')
# dictionary
theDict = {chr(y): y-65 for y in range(65, 91)}
# our ID's as Keys
keys = ["DBGEIGHIG", "DBGFCBEAA"]  # 3164876,316521400
my_key = keys[random.randint(-1, 1)]  # using one of the keys
# reading lines from txt
text2 = file2.readlines()
message = text2[0].upper()
encypt = text2[2].upper()


def vigenere_cipher_decrypt(plain_txt, key):
    cipher = ""
    new_code = key
    if len(plain_txt) > len(new_code):
        new_code += new_code[0:len(plain_txt) - len(new_code)]
    for x in range(0, len(plain_txt)):
        if ord(plain_txt[x]) in range(65, 91):
            cipher += (chr((((ord(plain_txt[x]) - 65) + (ord(new_code[x]) - 65)) % 26) + 65))
    print ('\n')
    return cipher


print vigenere_cipher_decrypt(message, my_key)


def key_finder(string):
    original_size = len(string)
    for x in range(1, original_size):  # take every word length from the size 1 to the original size of the word
        test_word = string[:x]
        count = 0
        temp_word = test_word
        for y in range(0, (original_size-len(test_word))):  # try and see if we take the word and extend it
                                                            # to the size of the original size if we get the same
                                                            # word so that's our key if at the end we didn't
                                                            # so that's the key used
            temp_word += test_word[count]
            count = (count + 1) % len(test_word)
        if temp_word == string:
            return test_word


def vigenere_cipher_key(plain_txt, cipher_txt):
    key = ""
    for x in range(0, len(plain_txt)):
        if ord(plain_txt[x]) in range(65, 91):
            key += (chr((((ord(cipher_txt[x]) - 65) - (ord(plain_txt[x]) - 65)) % 26) + 65))
    print key
    original_key = key_finder(key)
    print original_key, ",", len(original_key)


vigenere_cipher_key(message, vigenere_cipher_decrypt(message, my_key))
