s = input()
work_s = s.lower()
dictionary = {}
key_s = []
value_s = []
iterator = 0
alphabet = []
checker = 0

for i in range(len(work_s) - 1):
    if work_s:
        dictionary[work_s[0]] = work_s.count(work_s[0])
        work_s = work_s.replace(work_s[0], '')
    else:
        break

for key in dictionary.keys():
    key_s += str(key)

for value in dictionary.values():
    value_s += str(value)

key_s.sort()
value_s.sort(reverse=True)

for i in range(len(key_s)):
    alphabet += key_s[i]
    alphabet += str(dictionary[key_s[i]])

for i in range(len(value_s)):
    if checker != 3:
        print(alphabet[alphabet.index(value_s[i]) - 1], alphabet[alphabet.index(value_s[i])])
        del alphabet[alphabet.index(value_s[i]) - 1]
        del alphabet[alphabet.index(value_s[i])]
        checker += 1
    else:
        break
