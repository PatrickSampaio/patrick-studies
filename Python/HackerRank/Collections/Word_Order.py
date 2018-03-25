# https://www.hackerrank.com/challenges/word-order/problem
import sys 
import collections
data = list(sys.stdin.readlines())

knowed_words = set()
words_occurencies = collections.OrderedDict()

for dirty_word in data[1:len(data)]:
    word = dirty_word.replace('\n', '')
    if word in words_occurencies:
        words_occurencies[word] += 1
    else:
        words_occurencies[word] = 1
    
print(len(words_occurencies.keys()))

output = ''
for value in words_occurencies.values():
    output += ' {}'.format(value)
    
print(output.strip())
    
