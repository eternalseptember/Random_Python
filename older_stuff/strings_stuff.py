from modules.test import *
import string

def remove_vowels(s):
	vowels = "aeiouAEIOU"
	s_sans_vowels = ""
	for x in s:
		if x not in vowels:
			s_sans_vowels += x
	return s_sans_vowels

def find(str, ch, start=0, end=None):
	""" Find and return the index of ch in str.	Return -1 if ch does not occur in str. """
	ix = start
	if end is None:
		end = len(str)
	while ix < end:
		if str[ix] == ch:
			return ix
		ix += 1
	return -1

def count_letter(text, ch):
	count = 0
	for i in text:
		if i == ch:
			count += 1
	return(count)

def remove_punctuation(s):
	s_sans_punct = ""
	for letter in s:
		if letter not in string.punctuation:
			s_sans_punct += letter
	return s_sans_punct



test(remove_vowels("compsci") == "cmpsc")
test(remove_vowels("aAbEefIijOopUus") == "bfjps")
test(count_letter("banana", "a") == 3)
ss = "Python strings have some interesting methods."
test(find(ss, "s") == 7)
test(find(ss, "s", 7) == 7)
test(find(ss, "s", 8) == 13)
test(find(ss, "s", 8, 13) == -1)
test(find(ss, ".") == len(ss)-1)
test(remove_punctuation('"Well, I never did!", said Alice.') == "Well I never did said Alice")
test(remove_punctuation("Are you very, very, sure?") == "Are you very very sure")