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
    regexpr = f"([A-Za-z](({mister_or_mrs_reg}|{etc_reg}|{eg_reg}|{c_reg}|{ie_reg}|{initials_reg})|{not_punct_reg})*{punc_reg})"
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
    regexpr = f"([A-Za-z](({mister_or_mrs_reg}|{etc_reg}|{eg_reg}|{c_reg}|{ie_reg}|{initials_reg})|{not_punct_reg})*{punc_reg})"
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

def top_k_repeated_n_grams(sentences: list, n: int):
    list_of_grams = []
    for sentence in sentences:
        words = re.findall(r"[A-Za-z0-9]+", sentence)
        if len(words) >= n:
            for i in range(0, len(words) - n + 1):
                str = words[i]
                for m in range(i + 1, i + n):
                    str += ' ' + words[m]
                list_of_grams.append(str)
    dict_of_grams = dict()
    i = 1
    for gram in list_of_grams:
        dict_of_grams[gram] = list_of_grams.count(gram)

        # for k in range(i, len(list_of_grams)):
        #     if gram == list_of_grams[k]:
        #         list_of_grams.remove(list_of_grams.index(k))
        #         dict_of_grams[gram] += 1
        # i += 1
    return dict_of_grams

def main():
    while True:
        print("Write the text, which you want to parse.")
        text = str(input())
        print("Write n and k for task:")
        n = int(input())
        k = int(input())
        sentences = find_sentences(text)
        if len(sentences) == 0:
            print("Error. You entered not a sentence. Please enter it again correctly.")
            continue
        
        ngrams = top_k_repeated_n_grams(sentences, n)
        sorted_values = sorted(ngrams.values(), reverse=True) # Sort the values
        sorted_dict = {}

        for i in sorted_values:
            for j in ngrams.keys():
                if ngrams[j] == i:
                    sorted_dict[j] = ngrams[j]
                    break
        
        if k > len(sorted_dict):
            print("You entered a k more than a length of n-grams. We will just write full list of n-grams")
            k = len(sorted_dict)

        var = 1
        for key in sorted_dict:
            if var <= k:
                print(f"{key}: {sorted_dict[key]}")
                var += 1

        non_declarative_sentences = find_non_declarative_sentences(text)
        avg_length_of_sentence_ = avg_length_of_sentence(sentences)
        avg_length_of_word_ = avg_length_of_word(sentences)
        print(f"List of sentences:\n {sentences},\nList of non declarative sentences:\n {non_declarative_sentences},\nAverage number of characters in sentence: {avg_length_of_sentence_},\nAverage number of characters in word: {avg_length_of_word_}\n")
        print("Do you want to continue? [Y/N]")
        decision = input()
        if decision == "Y":
            continue
        else:
            break

if __name__ == "__main__":
    main()
#text = "Hello. My name is Dima. Your name is L. My name is."
    