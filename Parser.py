import re
import pytest

def find_sentences(text: str):
    mister_or_mrs_reg = r"([mM]r\.|[mM]rs\.)"
    etc_reg = r"(\setc\.\s[a-z])"
    eg_reg = r"(e\.g\.\s[a-z])"
    c_reg  = r"(\sc\.\s[a-z])"
    ie_reg = r"(i\.e\.\s[a-z])"
    initials_reg = r"([\s.][A-Z]\.(\s[A-Z]\.|\s[A-Z]))"
    not_punct_reg = r"([^\.\?\!])"
    punc_reg = r"((\.|\?|\!))"
    regexpr = f"([A-Z](({mister_or_mrs_reg}|{etc_reg}|{eg_reg}|{c_reg}|{ie_reg}|{initials_reg})|{not_punct_reg})*{punc_reg})"
    sentences_with_captured_groups = re.findall(regexpr,text)
    sentences = []
    for sentence in sentences_with_captured_groups:
        sentences.append(sentence[0])
    return sentences

def find_non_declarative_sentences(text: str):
    mister_or_mrs_reg = r"([mM]r\.|[mM]rs\.)"
    etc_reg = r"(\setc\.\s[a-z])"
    eg_reg = r"(e\.g\.\s[a-z])"
    c_reg  = r"(\sc\.\s[a-z])"
    ie_reg = r"(i\.e\.\s[a-z])"
    initials_reg = r"([\s.][A-Z]\.(\s[A-Z]\.|\s[A-Z]))"
    not_punct_reg = r"([^\.\?\!])"
    punc_reg = r"((\.))"
    regexpr = f"([A-Z](({mister_or_mrs_reg}|{etc_reg}|{eg_reg}|{c_reg}|{ie_reg}|{initials_reg})|{not_punct_reg})*{punc_reg})"
    sentences_with_captured_groups = re.findall(regexpr,text)
    sentences = []
    for sentence in sentences_with_captured_groups:
        sentences.append(sentence[0])
    return sentences

def avg_length_of_sentence(sentences: list):
    sum_of_characters = 0
    for sentence in sentences:
        chars = re.findall(r"[A-Za-z]", sentence)
        sum_of_characters += len(chars)
    return int(sum_of_characters / len(sentences)) 

def avg_length_of_word(sentences: list):
    number_of_words = 0 
    sum_of_characters = 0
    for sentence in sentences:
        number_of_words += len(sentence.split(' '))
        chars = re.findall(r"[A-Za-z]", sentence)
        sum_of_characters += len(chars)
    return int(sum_of_characters / number_of_words) 

# content of test_class.py
class TestClass:
    def test_one(self):
        assert find_sentences("Hello. My name is Mr. White. Also i am Heisenberg! I love S. White, my son and etc. boom.") == ["Hello.", "My name is Mr. White.", "Also i am Heisenberg!", "I love S. White, my son and etc. boom."]

    def test_two(self):
        assert find_non_declarative_sentences("Hello. My name is Mr. White. Also i am Heisenberg! I love S. White, my son and etc. boom.") == ["Hello.", "My name is Mr. White.", "I love S. White, my son and etc. boom."]

    def test_three(self):
        assert avg_length_of_sentence(["hello.", "hello!", "hello?"]) == 5

    def test_four(self):
        assert avg_length_of_word(["bla bla bla." "boo boo"]) == 3

print("Write the text, which you want to parse.")
text = str(input())
sentences = find_sentences(text)
non_declarative_sentences = find_non_declarative_sentences(text)
avg_length_of_sentence_ = avg_length_of_sentence(sentences)
avg_length_of_word_ = avg_length_of_word(sentences)
print(f"List of sentences:\n {sentences},\nList of non declarative sentences:\n {non_declarative_sentences},\nAverage number of characters in sentence: {avg_length_of_sentence_},\nAverage number of characters in word: {avg_length_of_word_}")