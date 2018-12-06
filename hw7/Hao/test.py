import numpy

def time2(x):
    return x * 2
li = [1,2,3]
for item in map(time2,li):
    print(type(item))
