from hash import Hash

flag = open('./flag.txt').read()

m1, m2 = input('m1> ')[:32], input('m2> ')[:32]

assert(len(m1) == 32)
assert(len(m2) == 32)

m1, m2 = [ord(x) % 256 for x in m1], [ord(x) % 256 for x in m2]

check = False
for x1, x2 in zip(m1, m2): 
    if x1 != x2:
        check = True
        break
assert(check)

h = Hash(5)

d1, d2 = h.hash(m1), h.hash(m2)

for x1, x2 in zip(d1, d2): assert(x1 == x2)

print('¯\_(ツ)_/¯')
print(flag)
