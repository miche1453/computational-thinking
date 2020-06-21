# computational-thinking
homework

In this assignment, you will revise two class definitions (Words and WordProcessor). Based on your WordProcessor definition, a WordProcessor object should be able to process a textual file by counting the number of words and extracting the vocabulary of words in the file content.

A word, in this assignment, is defined as a sequence of adjacent letters separated by punctuations, numbers, or white spaces. There is a method text_to_words() in class Words, which is capable of identifying words from a string. The method is applied in WordProcessor class definition to extract words.

Note that the vocabulary extracted by the WordProcessor object must consist of words without duplicates. This implies you have to remove repeated words when building the vocabulary. The method remove_dups() needs to be defined in class Words so that the method could be applied in class WordProcessor for vocabulary construction.

What is provided?
You are provided three files including

words.py, where class Words is defined. Task 1.

wp.py, where class WordProcessor and simple test code are presented. Task 2.

brooks.txt, the text file the test code in wp.py uses.

The brooks.txt file contains the statement:

“Show me your flowcharts and conceal your tables, and I shall continue to be mystified. Show me your tables, and I won't usually need your flowcharts; they'll be obvious.”

Separated by words it goes. The goal is the eliminate duplicates:

[‘show’, ‘me’, ‘your’, ‘flowcharts’, ‘and’, ‘conceal’, ‘tables’, ‘I’, ‘shall’, ‘continue’, ‘to’, ‘be’, ‘mystified’, ‘won’, ‘t’, ‘usually’, ‘need’, ‘they’, ‘ll’, ‘obvious’]
