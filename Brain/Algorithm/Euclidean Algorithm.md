---

---
# Euclidean Algorithm
- 두 수의 최대공약수를 구하는 방법
- 큰 수를 작은 수로 나누고, 나머지를 이용해 원래의 작은 수와 나머지로 또 나누는 과정을 반복
- 이 때, 나머지가 0이 되면, 그 때의 작은 수가 최대공약수가 됨

---
# 파이썬
```python
# 최대공약수
def GCM(a,b):
    while a%b!=0:
        a=a%b
        a,b=b,a 
    return b

# 최소공배
def LCM(a,b):
    return (a*b)//GCM(a,b)
```