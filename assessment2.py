#write a function that takes a list of random string(containing numbers and other datatype)
#and create a new list containing only the words(alphabetic strings) from the input list.

def alphabetic_strings(strings):
    alphabetic=[]
    for string in strings:
        if string.isalpha():
            alphabetic.append(string)
            
    return alphabetic



strings= ['ahhhh', "552211", 'hello world', 'x1253','1342']
alphabetic = alphabetic_strings(strings)
print(alphabetic)
    