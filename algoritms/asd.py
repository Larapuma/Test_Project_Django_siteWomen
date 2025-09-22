def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    arr = [0, 1, 1]
    for i in range(2, n):
        summ = sum(arr[len(arr)-2:len(arr)])

        arr.append(summ)
    return arr[-1]


def fib_2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)

for i in range(21):
    print(fib(i))

for i in range(21):
    print(fib_2(i))




def func(l:list)->int:
    res = 0
    i = 0
    while  True:
        if(l[i]==2):
            res+=(l[i+1]*l[i+2])
            i+=3
        elif(l[i]==1):
            res+=l[i+1]+l[i+2]
            i += 3
        else:
            return res

arr = [1,2,4,2,3,3,2,9,3,99,2,1,24]
print(func(arr))

def f(l:list)->int:
    res = 0
    i = 0
    n = len(l)
    while i<n:
        if l[i] == 1:
            if i+2>=n:
                return res
            res += l[i + 1] + l[i + 2]
            i+=3
        elif l[i] == 2:
            if i+2>=n:
                return res
            res += (l[i + 1] * l[i + 2])
            i+=3
        elif l[i] == 99:
            return res
        else:
            i+=1
    return res

print(f(arr))
print(f([]))
print(f([1,1,1,99]))
print(f([99]))
print(f([2,2,2,99]))


