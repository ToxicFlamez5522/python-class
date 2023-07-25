#1 write a function that takes a list of sentences and gets the sentence
#with the longest number of words.
def longest_sentences(sentences):
    longest = ' '
    for sentence in sentences:
        if len(sentence.split(' ')) > len(longest.split(' ')):
            longest = sentence
    return longest 

sentences=['I am a boy', 'my name is fortune', 'python is difficult', 'why do i feel so tired']
longest = longest_sentences(sentences)
print(longest)      