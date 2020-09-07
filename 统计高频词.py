a = 'w w w c c h h i i i i i '
aList = a.split()

def histogram(a):
    d = {}
    for b in a :
        if b in d:
            d[b] += 1
        else:
            d[b] = 1
    return d

h = histogram(aList)
print(h)

def show(wordsDict):
    dictList = []
    for key,val in wordsDict.items():
        dictList.append((val,key))
    dictList.sort(reverse = True)
    print('%-10s%10s' %('word','count'))
    print('-'*25)
    for val,key in dictList:
        if val > 10:
            print('%-12s         %3d' % (key,val))

h = histogram(aList)
show(h)
