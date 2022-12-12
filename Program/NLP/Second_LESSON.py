import string
import re
from nltk.tokenize import word_tokenize
from nltk import pos_tag , ne_chunk
import nltk
import tkinter

def Speech_Tagging(text):
    word_part = word_tokenize(text)
    return pos_tag(word_part)



def chunking(text, grammar):
    word_token = word_tokenize(text)
    word_pos = pos_tag(word_token)
    chunkParser = nltk.RegexpParser(grammar)
    tree = chunkParser.parse(word_pos)

    for subtree in tree.subtrees():
        print(subtree)
    tree.draw()

def name_entity_recognition(text):
    word_token = word_tokenize(text)
    word_pos = pos_tag(word_token)
    print(ne_chunk(word_pos),"\n")

if __name__ == '__main__':
    print("Starting Main Function")
    input_First = "You just gave me a scare"
    print(Speech_Tagging(input_First),"\n")
    sentence = "the little yellow bird is flying in the sky"
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    # chunking(sentence,grammar)
    another_text = "Bill works for GeeksforGeeks so he went to Delhi for a meetup."
    name_entity_recognition(another_text)
