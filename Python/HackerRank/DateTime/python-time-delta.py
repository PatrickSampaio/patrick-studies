https://www.hackerrank.com/challenges/python-time-delta/problem

import sys
from datetime import datetime

def time_delta(t1, t2):
    # Complete this function
    first_date = datetime.strptime(t1, '%a %d %b %Y %X %z')
    second_date = datetime.strptime(t2, '%a %d %b %Y %X %z')
    return abs(int((first_date - second_date).total_seconds()))

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        print(time_delta(input().strip(), input().strip()))
        
