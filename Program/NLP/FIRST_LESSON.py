import re
import string
import inflect
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

def lowerCase(text):
    split_text = text.split()
    p = inflect.engine()
    new_string = []
    for sample_text in split_text:
        if sample_text.isdigit():
            temp = p.number_to_words(sample_text)
            new_string.append(temp)
        else:
            new_string.append(sample_text)
    print(new_string,"\n")
    temp_str = ' '.join(new_string)
    print(temp_str,"\n")
    return text.lower()

def remove_punctuations(text):
    translator = str.maketrans('','',string.punctuation)
    return text.translate(translator)

def remove_whitespace(text):
    return ' '.join(text.split())

def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    word_tokens= word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return filtered_text

def stem_words(text):
    stemmer = PorterStemmer()
    word_tokens = word_tokenize(text)
    stems= [stemmer.stem(word) for word in word_tokens]
    return stems

def lemmatize_word(text):
    lemmatizer = WordNetLemmatizer()
    word_tokens = word_tokenize(text)
    lemmas = [lemmatizer.lemmatize(word, pos='v') for word in word_tokens ]
    return lemmas

if __name__ == "__main__":
    input_str = "Hey, did you know that the summer break is coming? Amazing right !! It's only 5 more days !!"
    another_string_contain_whitespace = "   we don't need   the given questions"
    example_text = "This is a sample sentence and we are going to remove the stopwords from this."
    stem_text = "data science uses scientific methods algorithms and many types of processes"
    print(lowerCase(input_str),"\n")
    print(remove_punctuations(input_str),"\n")
    print(remove_whitespace(another_string_contain_whitespace),"\n")
    print(remove_stopwords(example_text),"\n")
    print(stem_words(stem_text),"\n")
    print(lemmatize_word(stem_text))