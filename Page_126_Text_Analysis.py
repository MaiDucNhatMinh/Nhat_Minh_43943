"""
Author: Mai Duc Nhat Minh
Date: 25/09/2021
Problem:  This program will perform the following tasks:
1. Receive the filename from the user, open the file for input, and input the text.
2. Count the sentences in the text.
3. Count the words in the text.
4. Count the syllables in the text.
5. Compute the Flesch Index.
6. Compute the Grade Level Equivalent.
7. Print these two values with the appropriate labels, as well as the counts from
tasks 2–4.
Solution:

    ....
"""
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()
sentences = text.count('.') + text.count('?') + \
 text.count(':') + text.count(';') + \
 text.count('!')
words = len(text.split())
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
 for vowel in vowels:
    syllables += word.count(vowel)
 for ending in ['es', 'ed', 'e']:
    if word.endswith(ending):
        syllables -= 1
    if word.endswith('le'):
        syllables += 1
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = round(0.39 * (words / sentences) + 11.8 * \
        (syllables / words) - 15.59)
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")
sentences = int(input("Sentences: "))
words = int(input("Words: "))
syllables = int(input("Syllables: "))
