"""
There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one
edit (or zero edits) away.
"""


def one_away(str1, str2):
	# character replacement
	# check this first because the strings need to be equal

	# insert a character

	# remove a character


	return True


def check_replace(str1, str2):
	# string length should be equal
	# only one character should be changed
	return True


def check_insert(str1, str2):
	# string sizes could also equal
	# return True if str2 inserted a character
	# and no other characters are have been changed
	return True


def check_remove(str1, str2):
	# string sizes could also equal
	# return True if str2 removed a character
	return True




# true, true, true, false
str_1_set = ['pale', 'pales', 'pale', 'pale']
str_2_set = ['ple', 'pale', 'bale', 'bake']

sets = 4
for i in range(sets):
	str_1 = str_1_set[i]
	str_2 = str_2_set[i]

	result = one_away(str_1, str_2)
	print(result)


