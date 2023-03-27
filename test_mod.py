#from Parser import (find_sentences, find_non_declarative_sentences, avg_length_of_sentence, avg_length_of_word)
import pytest
import Parser as Ps

# content of test_class.py
#class TestClass:

def test_one():
    assert Ps.find_sentences("Hello. My name is Mr. White. Also i am Heisenberg! I love S. White, my son and etc. boom.") == ["Hello.", "My name is Mr. White.", "Also i am Heisenberg!", "I love S. White, my son and etc. boom."]

def test_two():
    assert Ps.find_non_declarative_sentences("Hello. My name is Mr. White. Also i am Heisenberg! I love S. White, my son and etc. boom.") == ["Hello.", "My name is Mr. White.", "I love S. White, my son and etc. boom."]

def test_three():
    assert Ps.avg_length_of_sentence(["hello.", "hello!", "hello?"]) == 5

def test_four():
    assert Ps.avg_length_of_word(["bla bla bla." "boo boo"]) == 3
