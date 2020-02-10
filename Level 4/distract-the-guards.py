from fractions import gcd

def checkList(array, u):
    count = 0
    for p in range(3):
        for i in range(len(array)/2):
            for j in list(reversed(range(i,len(array)))):
                if j <= len(array)-1 and j > i and j != i:
                    if is_forever(array[i],array[j]):
                        if(0 <= i <= len(array) and len(array) > 0):
                            u.append(array.pop(i))
                            count += 1
                        if(0 <= j <= len(array) and len(array) > 0):
                            u.append(array.pop(j-1))
                            count += 1
    return count

def validate(banana_list):
    if len(banana_list) > 100:
        temp = []
        counter = 0
        for i in banana_list:
            if counter <= 100:
                temp.append(i)
                counter += 1
        banana_list = temp
    elif len(banana_list) <= 1:
        return len(banana_list)
    for i in banana_list:
        if 1 > i or i >= 2**30:
            banana_list.pop(i)

def solution(banana_list):
    validate(banana_list)
    banana_list = list(banana_list)
    banana_list.sort()
    orig = []
    for i in banana_list:
        orig.append(i)
    u = []
    count1 = checkList(banana_list, u)
    return len(orig) - count1

def is_forever(x, y):
    z = (x + y) / gcd(x, y)
    return bool((z - 1) & z)