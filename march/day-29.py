from collections import defaultdict

'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3,
since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable.
For example, '001' is not allowed.

a-a-a-a
a-a-k
a-k-a

k-a

111:
     1 - decode(11)
     1 - decode(1)-decode(1)
    11 - decode(1)
'''


def sliceNumber(n, distance):
    if (len(str(n)) < distance):
        return 0
    return int(str(n)[distance:])


def decode(s):
    if s.startswith('0'):
        return 0
    elif len(s) <= 1:  # This covers empty string
        return 1

    total = 0

    if int(s[:2]) <= 26:
        total += decode(s[2:])

    total += decode(s[1:])
    return total


'''
[{ 5: 1 }]

'''


def decode2(s):
    cache = defaultdict(int)
    cache[len(s)] = 1
    cache[len(s) - 1] = 1
    reversedDomain = reversed(range(len(s)))

    for i in reversedDomain:

        if int(s[i:i + 2]) <= 26:
            cache[i] = cache[i + 2]
        cache[i] += cache[i + 1]
        print(cache)

    return cache[0]


# print(decode('111'))
print(decode("28111"))
print(decode2("28111"))
