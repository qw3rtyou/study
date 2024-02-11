from z3 import *

# 변수 정의
key = [Int("key[%d]" % i) for i in range(21)]

# SMT Solver 생성
s = Solver()

# 주어진 조건에 따라 제약 조건 추가
s.add(key[1] == key[4])
s.add(key[5] == 118)
s.add(key[6] == 162)
s.add(key[18] == 168)
s.add((key[0] % 100 - 6) == key[10])
s.add(key[2] % 100 == 34)
s.add((key[2] + key[6]) * 2 == 592)
s.add(key[4] % 100 == 30)
s.add(key[5] < key[6])
s.add(key[5] < key[11])
s.add(key[7] % 100 == 74)
s.add(key[8] == key[18])
s.add(key[9] == key[4])
s.add(key[9] > key[10])
s.add(key[10] % 100 == 80)
s.add(key[11] == key[12])
s.add((key[12] + key[1]) * 2 == 528)
s.add(key[13] > key[18])
s.add(key[15] % 100 == 48)
s.add((key[15] + key[16] * 2 - key[17]) == 226)
s.add((key[15] + key[14]) / 2 == 148)
s.add(key[19] < key[0])
s.add(key[15] > key[16])
s.add(key[17] % 100 == 78)
s.add((key[16] * key[5] / 4) == 2301)
s.add(key[3] + key[10] + key[8] == 406)
s.add(key[20] + key[15] == 154)
s.add(key[19] == key[20])
s.add(key[7] > key[8])
s.add(key[15] > key[16])
s.add(key[15] < key[7])
s.add(key[14] > key[0])
s.add((key[12] + key[13] + key[14]) == 454)

if s.check() == sat:
    m = s.model()
    res = []
    for i in range(21):
        res.append(m.evaluate(key[i]))
        print("%d" % (m.evaluate(key[i])), end="")
    print(res)
else:
    print("제약 조건을 만족하는 키를 찾을 수 없습니다.")
