from Parser import (find_sentences, find_non_declarative_sentences, avg_length_of_sentence, avg_length_of_word)
import pytest

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
