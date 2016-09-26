from modules.test import *
from modules.searches import *
import time

'''
xs = [1,3,5,7,9,11,13,15,17,19]
ys = [4,8,12,16,20,24]
zs = xs + ys
zs.sort()

test(merge(xs, []) == xs)
test(merge([], ys) == ys)
test(merge([], []) == [])
test(merge(xs, ys) == zs)
test(merge([1,2,3], [3,4,5]) == [1,2,3,3,4,5])
test(merge(["a", "big", "cat"], ["big", "bite", "dog"]) 
	== ["a", "big", "big", "bite", "cat", "dog"])
'''

bigger_vocab = load_words_from_file("vocab.txt")

all_words = get_words_in_book("alice_in_wonderland.txt")
t0 = time.clock()
all_words.sort()
book_words = remove_adjacent_dups(all_words)
missing_words = find_unknown_merge_pattern(bigger_vocab, book_words)
t1 = time.clock()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))

