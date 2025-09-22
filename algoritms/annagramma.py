def is_anagram(a, b):
    if len(a) != len(b): return False
    arr = [0] * 33
    a = a.lower()
    b = b.lower()
    for i in range(len(a)):
        arr[ord(a[i]) - ord('а')] += 1
        arr[ord(b[i]) - ord('а')] += 1
    for i in range(26):
        if arr[i] % 2 != 0: return False
    return True


def is_all_unique(lst):
    if not lst: return True
    dict_nums = dict()
    for num in lst:
        dict_nums.setdefault(num,0)
        dict_nums[num]+=1
        if dict_nums[num]>1: return False
    return True

print(is_all_unique([1,2,3,4,5]))


def get_simple_numbers(n):
    arr = [True] * n
    res = []
    for i in range(2,n):
        if arr[i]:
            res.append(i)
            for j in range(i*i, n, i):
                arr[j] = False
    return res
print(get_simple_numbers(10))


def rle_encode(message):
    res = ""
    counter = 1
    char = message[0]
    for i in range(1, len(message)):
        if char == message[i]:
            counter += 1
        else:
            res += char + str(counter)
            char = message[i]
            counter = 1
    res+= char +str(counter)
    return res
print(rle_encode('AAAABBCAA'))


def reverse_vowels(s):
    vowels = "аеёиоуэюяыАЕЁИОУЭЮЯЫAEIOUaeiou"
    arr = list(s)
    left = 0
    right = len(arr) - 1

    while left < right:

        while left < right and arr[left] not in vowels:
            left += 1


        while left < right and arr[right] not in vowels:
            right -= 1


        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return ''.join(arr)


# Тестирование
print(reverse_vowels("Carthago delenda est"))  # "Certhage delonda ast"


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



for i in range(10):
    print(fib(i))

ar = [1,2,3]
print(sum(ar[len(ar)-2:len(ar)]))


def postfix_duplicates(str):
    arr = str.split()
    d = dict()
    for i in range(len(arr)):
        d.setdefault(arr[i], 0)
        if d[arr[i]] == 0:
            d[arr[i]] += 1
            continue
        d[arr[i]] += 1
        arr[i] = arr[i] + f"_{d[arr[i]]-1}"

    return ' '.join(arr)

print(postfix_duplicates("a a a b c a a d c d d"))


def is_armstrong_number(num):
    arr = []
    size = 0
    copy = num
    while copy != 0:
        size += 1
        arr.append(copy % 10)
        copy //= 10

    res = 0
    for i in range(len(arr)):
        res += arr[i] ** size
    return res == num
print(is_armstrong_number(371)) # True


def get_last_survivor_index(n, k):
    arr = [i  for i in range(n)]
    c = 1
    while len(arr) != 1:
        arr.pop(((k * c)-1) % len(arr))
        c+=1
    return arr[0]+1
print(get_last_survivor_index(5, 2) )# 3

def decimal_to_binary(decimal):
    res = ''
    while decimal != 0:
        if decimal%2==0:
            res+="0"
        else:
            res+="1"
        decimal//=2
    return res[::-1]
print(decimal_to_binary(8))

a = {'a':2,'b':3,}
b = set(a)
c = set({'a':3})
print(type(a.keys()))
