## https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(''.join([list(string[i:i+k])[index] \
            if list(string[i:i+k])[index] not in list(string[i:i+k])[:index] else '' \
            for index in range(0, len(list(string[i:i+k])))]))
        
