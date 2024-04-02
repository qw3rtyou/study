# 참고
[[유전 알고리즘을 이용한 Substitution Cipher 복호화]]

---
# Generic Algorithm(GA)

1. **초기 인구 생성:** 문제의 가능한 해들로 구성된 초기 집합(인구)을 무작위로 생성합니다. 각 해는 '염색체(chromosome)'로 표현되며, 이는 보통 이진 문자열이나 다른 데이터 구조가 될 수 있습니다.

2. **적합도 평가(Fitness Evaluation):** 인구 내의 각 개체(해)에 대해, 그 해의 적합도(문제를 얼마나 잘 해결하는지에 대한 점수)를 평가합니다.

3. **선택(Selection):** 적합도에 따라 개체들을 선택합니다. 높은 적합도를 가진 개체는 다음 세대에 자신의 유전 정보를 전달할 확률이 더 높습니다.

4. **교차(Crossover):** 선택된 개체들을 조합하여 새로운 개체(자식)를 생성합니다. 이 과정에서 두 개체의 유전 정보를 교환하여 새로운 해를 만듭니다.

5. **돌연변이(Mutation):** 낮은 확률로 자식 개체의 일부 유전 정보를 무작위로 변경합니다. 이는 탐색 공간을 넓혀주고 지역 최적해에 갇히는 것을 방지하는 역할을 합니다.

6. **새로운 세대 생성:** 새로운 개체들로 이루어진 다음 세대를 생성합니다. 이 과정에서 일부 구세대 개체는 새로운 개체로 대체됩니다.

7. **종료 조건 검사:** 특정 종료 조건(예: 최대 세대 수 도달, 적합도 점수가 특정 값 이상, 일정 세대 동안 개선이 없음 등)을 만족할 때까지 2~6단계를 반복합니다.

---