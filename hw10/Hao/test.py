#!/usr/local/bin/python3


li1 = [True,False,False,True]
li2 = [True,True,False,True]
ergs = [1 if li1[i] == li2[i] else 0 for i in range(len(li1))]
print(sum(ergs)/len(ergs))



def sortieren(li):
    res = [li[0]]
    for i in li[1:]:
        insert_index = 0
        for index in range(len(res)):
            if i >= res[index]:
                insert_index += 1
        res.insert(insert_index, i)
    return res
