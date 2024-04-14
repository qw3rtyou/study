# 키워드
- 정적 분석

# 코드
- main.c
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v3; // cl
  int v4; // edx
  int v5; // ecx
  int v6; // er8
  int v7; // er9
  bool v8; // cf
  bool v9; // zf
  int v10; // edx
  __int64 v11; // rcx
  const char *v12; // rsi
  char *v13; // rdi
  char _0[40]; // [rsp+0h] [rbp+0h] BYREF
  unsigned __int64 vars28; // [rsp+28h] [rbp+28h]

  vars28 = __readfsqword(0x28u);
  _printf_chk(1, (unsigned int)"Input: ", (_DWORD)envp, v3);
  _isoc99_scanf((unsigned int)"%26s", (unsigned int)_0, v4, v5, v6, v7, _0[0]);
  shift_right(_0, 3LL);
  xor_with_key(_0, off_4E50F0);
  shift_left(_0, 3LL);
  xor_with_key(_0, off_4E50F0);
  shift_right(_0, 3LL);
  v11 = 26LL;
  v12 = "|l|GHyRrsfwxmsIrietznhIhj";
  v13 = _0;
  do
  {
    if ( !v11 )
      break;
    v8 = (unsigned int)*v12 < (unsigned __int8)*v13;
    v9 = *v12++ == (unsigned __int8)*v13++;
    --v11;
  }
  while ( v9 );
  if ( (!v8 && !v9) == v8 )
    _printf_chk(1, (unsigned int)"Correct!", v10, v11);
  else
    _printf_chk(1, (unsigned int)"KKKKKKKKKKKKK", v10, v11);
  return 0;
}
```




# 풀이

- 딱히 연산간에 의존성이 없어 그대로 역산하면 됨

```python
def shift_right(text, num):
    a = text[-num:]
    b = text[:-num]
    return a + b


def shift_left(text, num):
    a = text[:num]
    b = text[num:]
    return b + a


def xor_with_key(text, key):
    text_bytes = text.encode()
    key_bytes = key.encode()

    result = bytearray(len(text_bytes))

    for i in range(len(text_bytes)):
        result[i] = text_bytes[i] ^ key_bytes[i % len(key_bytes)]

    return result.decode()


if __name__ == "__main__":
    cipher = "GHyRrsfwxmsIrietznhIhj"
    key = "qksrkqs"

    cipher = shift_left(cipher, 3)
    cipher = xor_with_key(cipher, key)
    cipher = shift_right(cipher, 3)
    cipher = xor_with_key(cipher, key)
    cipher = shift_left(cipher, 3)
    print(cipher)

```

# flag
```
>python3 exploit.py
DH{ShiftxorShiftxorShift}
```