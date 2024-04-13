# 코드
```python
from sympy.ntheory import factorint
from sympy import mod_inverse

n = 3174654383
e = 65537
C = 2487688703

factors = factorint(n)
p, q = factors.keys()

phi_n = (p - 1) * (q - 1)

d = mod_inverse(e, phi_n)

M = pow(C, d, n)

print(f"Plaintext (M): {M}")
print(f"Private Key (d): {d}")

plaintext_int = M

plaintext_bytes = plaintext_int.to_bytes(4, 'big')
plaintext_str = plaintext_bytes.decode('ascii')

print(plaintext_str)
```


# 결과
``` sh
$ python3 exploit.py 
Plaintext (M): 1198485348
Private Key (d): 801567233
Good
```