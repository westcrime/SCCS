import re

text = "Hello. My name is Mr. White. Also i am Heisenberg! I love S. White, my son and etc. boom."

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

print(find_sentences(text))
print(find_non_declarative_sentences(text))