# I used these websites to assist me in writing this code:
# https://codereview.stackexchange.com/questions/183658/replacing-letters-with-numbers-with-its-position-in-alphabet
# https://favtutor.com/blogs/reverse-dictionary-python
# Various pages on W3Schools, to review basic Python concepts

from string import ascii_lowercase

# This first part of the program was an attempt to use the encryption method
# described in the handout, but I didn't succeed with it.

letter_num_legend = {'a':'00','b':'01','c':'02','d':'03','e':'04','f':'05','g':'06','h':'07','i':'08',
        'j':'09','k':'10','l':'11','m':'12','n':'13','o':'14','p':'15','q':'16','r':'17',
        's':'18','t':'19','u':'20','v':'21','w':'22','x':'23','y':'24','z':'25'}

num_letter_legend = {}
for key in letter_num_legend:
    value = letter_num_legend[key]
    num_letter_legend[value] = key

# This function takes in a string of letters and outputs the corresponding string of numbers.
def letters_to_numbers(plaintext):

    # Since we don't really care about case, to make the code simpler,
    # I'm putting all the text in lowercase.
    plaintext.lower()

    for current_letter in ascii_lowercase:
        number = letter_num_legend.get(current_letter)
        plaintext = plaintext.replace(current_letter,number)

    return plaintext

def numbers_to_letters(numstring):
    numarray = ['00','01','02','03','04','05','06','07','08','09','10',
                '11','12','13','14','15','16','17','18','19','20','21',
                '22','23','24','25']

    for current_number in numarray:
        letter = num_letter_legend.get(current_number)
        numstring = numstring.replace(current_number,letter)
    return numstring

# I'm not sure how to actually use this, since I needed to use numbers as strings
# in order to say that a is 00 rather than just 0. But then I don't know how to
# do arithmetic. But I won't delete this, since it was part of the process
# of figuring it out. Here is another attempt that worked better.

# Given a letter, this dictionary tells us the corresponding number
alphabet_dictionary = {}
counter = 0
for letter in ascii_lowercase:
    alphabet_dictionary[letter] = counter
    counter += 1

# Given a number, this dictionary tells us the corresponding letter
reverse_alphabet_dictionary = {}
for key in alphabet_dictionary:
    value = alphabet_dictionary[key]
    reverse_alphabet_dictionary[value] = key

# This defines a function which performs a shift for us. It can be used
# either to convert plaintext to ciphertext or vice versa.
def shift_by_n(input, n):
    input.lower()
    output = ''
    cipherletter = ''
    for current_letter in input:
        original_number = alphabet_dictionary[current_letter]
        shifted_number = (original_number + n) % 26
        cipherletter = reverse_alphabet_dictionary[shifted_number]
        output = output + cipherletter
    print(output)
    return output

# This is how I solved the cipher of unknown shift. Those with more
# patience than I have may benefit from looking for patterns,
# instead of my brute force approach.
for i in range(26):
    shift_by_n('eduyiademdqiqkdyj',i)
        
