import random
import string
# print(random.choices(string.ascii_letters, k=6))
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
def encode_message(message):
    words= message.split()
    encoded_words= [encode_word(word) for word in words]
    return ''.join(encoded_words)
def encode_word(word):            
    #Professional method:
    if len(word)>=3:
        encoded_word= word[1:]+ word[0]
#   now append three random characters at the starting and the end
        last_random= ''.join(random.choices(string.ascii_letters, k=3))
        first_random= ''.join(random.choices(string.ascii_letters, k=3))
        encoded_word= first_random+encoded_word+last_random        
# else:
#   simply reverse the string
    else:
        encoded_word= word[::-1]
    return encoded_word+' '

# Decoding:
def decode_message(Encoded_message):
    words2= Encoded_message.split()
    decoded_words= [decode_words(word2) for word2 in words2]
    return ''.join(decoded_words)
def decode_words(word2):
# if the word contains less than 3 characters, reverse it
    if len(word2)<3:
        decoded_word=word2[::-1]
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
    else:
        trimmed_word2= word2[3:len(word2)-3]
        decoded_word= trimmed_word2[-1]+trimmed_word2[0:-1]
    return decoded_word+' '



# main
# Your program should ask whether you want to code or decode

User_choice_DecOrEnc= input('What Do you want this program to do :\n\t(i)Enter \'D\' to Decode\n\t(ii) Enter \'E\' to Encode\n\n')
#Error handling
if User_choice_DecOrEnc.upper()=='E':
    User_message_toEncode= input('Type your message here :\n')
    Endoced_output= encode_message(User_message_toEncode)
    print('Encoded Script : \n',Endoced_output)
elif User_choice_DecOrEnc.upper()=='D':
    User_message_toDecode = input('enter the sentence to be decoded :\n')
    Decoded_output= decode_message(User_message_toDecode)
    print('Decoded Script : \n',Decoded_output)
else:
    raise ValueError ('Plese Enter only E or D as your choice')