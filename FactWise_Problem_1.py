maps = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 20: 6, 30: 6, 40: 5, 50: 5, 60: 6,
        70: 7, 80: 6, 90: 6, 100: 7, 1000: 8, 'and': 3, 'teen': 4}


def int_to_list(number):
    c = []
    s = str(number)
    for dgt in s:
        a = int(dgt)
        c.append(a)
    return c


def list_to_int(numList):
    s = map(str, numList)
    s = ''.join(s)
    s = int(s)
    return s


L = []
for i in range(1, 1001, 1):
    L.append(i)


def one_digit(n):
    q = maps[n]
    return q


def eleven(n):
    q = maps[11]
    return q


def teen(n):
    digits = int_to_list(n)
    q = maps[digits[1]] + maps['teen']
    return q


def two_digit(n):
    digits = int_to_list(n)
    first = digits[0]
    first = first * 10
    second = digits[1]
    q = maps[first] + one_digit(second)
    return q


def three_digit(n):
    digits = int_to_list(n)
    first = digits[0]
    second = digits[1]
    third = digits[2]

    f = maps[first] + maps[100]

    if second == 1 and third == 1:
        s = maps['and'] + maps[11]
    elif second == 1 and third != 1:
        s = digits[1:]
        s = list_to_int(s)
        s = maps['and'] + teen(s)
    elif second == 0 and third == 0:
        s = maps[0]
    elif second == 0 and third != 0:
        s = maps['and'] + maps[third]
    else:
        s = digits[1:]
        s = list_to_int(s)
        s = maps['and'] + two_digit(s)

    q = f + s
    return q

def thousand(n):
    q = maps[1000]
    return q


lengths = []

for i in L:
    if i < 11:
        n = one_digit(i)
        lengths.append(n)
    elif i == 11:
        n = eleven(i)
        lengths.append(n)
    elif 11 < i < 20:
        n = teen(i)
        lengths.append(n)
    elif 20 < i < 100:
        n = two_digit(i)
        lengths.append(n)
    elif 100 <= i < 1000:
        n = three_digit(i)
        lengths.append(n)
    elif i == 1000:
        n = thousand(i)
        lengths.append(n)
    else:
        pass

# since "eighteen" has eight letters (not 9), subtract 10
sumWords = sum(lengths) - 10
print("Your number is: ", sumWords)
