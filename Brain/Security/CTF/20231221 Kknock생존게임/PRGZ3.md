# 키워드
- Python Z3

---
# 문제 배경
- 플레이어가 최종 보스를 물리쳤을 때 엔딩크레딧이 잠깐 올라오고 여기에 key(flag)가 출력되게 됨
```c
if (tMonster.iHP <= 0)
{
	printf("%s is dead\n", tMonster.strName);


	tPlayer.iExp += tMonster.iExp;
	int iGold = (rand() % (tMonster.iGoldMax - tMonster.iGoldMin + 1) +
		tMonster.iGoldMin);
	tPlayer.tInventory.iGold += iGold;

	printf("Gain Exp: %d\n", tMonster.iExp);
	printf("%d Gain Gold\n", iGold);
	if (tMonster.iLevel == 999)
	{
		printf("=======Ending======== \n \n");
		int j = 0;
		for (j = 0; j < 21; j++)
		{

			printf("%c", (key[j] + 60) / 2);

		}
		printf("\n");
		printf("=====================\n\n");
		system("pause");
		return 0;
	}
	tPlayer.iHP = tPlayer.iHPMax;
	tPlayer.iMP = tPlayer.iMPMax;
	tMonster.iHP = tMonster.iHPMax;
	tMonster.iMP = tMonster.iMPMax;
	alive = 0;
	system("pause");
	break;
}
```

- `Secret_Command` 함수를 만족하는 모든 키를 사용자가 입력했을 때 온전한 flag가 출력되게 만들어놨음
```c
void Secret_Command(int a)
{
	int token = 0;
	key[iasdf++] = a;
	if (iasdf > 20) {
		printf("======================CheatMode======================\n");
		if ((key[1]) == key[4] && key[5] == 118)
			token++;
		if (key[6] == 162 && key[18] == 168)
			token++;
		if ((((key[0] % 100) - 6)) == key[10])
			token++;
		if ((key[2] % 100) == 34)
			token++;
		if (((key[2] + key[6]) * 2) == 592)
			token++;
		if (((key[4] % 100) == 30))
			token++;
		if (key[5] < key[6] && key[5] < key[11])
			token++;
		if (((key[7] % 100) == 74))
			token++;
		if (key[8] == key[18] && key[9] == key[4])
			token++;
		if (key[9] > key[10] && key[0] < key[1])
			token++;
		if ((key[10] % 100) == 80)
			token++;
		if ((key[11]) == key[12])
			token++;
		if (((key[12] + key[1]) * 2) == 528)
			token++;
		if (key[13] > key[18] && key[2] > key[0])
			token++;
		if ((key[15] % 100) == 48)
			token++;
		if (((key[15] + key[16] * 2 - key[17])) == 226)
			token++;
		if ((((key[15] + key[14]) / 2)) == 148)
			token++;
		if (key[19]<key[0] && key[15] > key[16])
			token++;
		if (((key[17] % 100) == 78))
			token++;
		if ((key[16] * key[5] / 4) == 2301)
			token++;
		if ((key[3] + key[10] + key[8]) == 406)
			token++;
		if (key[20] + key[15] == 154 && key[19] == key[20])
			token++;
		if (key[7] > key[8] && key[15] > key[16])
			token++;
		if (key[15]<key[7] && key[14]>key[0])
			token++;
		if ((key[12] + key[13] + key[14]) == 454)
			token++;
	}
	if (token == 25)
	{

		tPlayer.tInventory.iGold = 999999;
		system("pause");

	}


}
```

- 따라서 위의 모든 로직을 통과하는 key값을 구해야 하는데 이는 직접할 수도 있겠지만 z3 같은 모듈로 쉽게 해결할 수 있음


# Poc코드
- 아래 코드 실행 결과를 상점 선택창에서 하나씩 입력하면 flag가 나오게 됨
``` python
from z3 import *

# 변수 정의
key = [Int('key[%d]' % i) for i in range(21)]

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
```

