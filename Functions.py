from math import *
from random import randint
import statistics

list1 = []
list2 = []
x=int

def inputlist():
    ###list###
    global x
    x = int(input("How many numbers: "))
    for a in range(x):
        list1.append(randint(1, 100))
    print("The set of numbers is", list1)
    ###maximum###
    maxl = max(list1)
    print("The largest number is", maxl)
    ###minimum###
    minl = min(list1)
    print("The smallest snumber is", minl)
    ###average###
    average = sum(list1)/len(list1)
    print("The average is", average)
    ###mediah###
    sort = sorted(list1)
    med = statistics.median(sort)
    print("The median is", med)
    ###stdev###
    i = 0
    for i in range(len(list1)):
        x = (list1[i]-average)**2
        list2.append(x)
    y = sum(list2)
    z = len(list1)
    stdev = sqrt(y/z)
    print("The standard deviation is", stdev)

inputlist()