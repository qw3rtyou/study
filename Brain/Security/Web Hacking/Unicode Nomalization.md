# Unicode Nomalization
- 문자열의 다양한 가능한 표현을 일관된 형태로 통일하는 과정
- 동일한 글자나 글자 조합도 여러 가지 다른 코드 포인트 조합으로 인코딩될 수 있음

- 유니코드 정규화에는 주로 네 가지 형태가 있다고 함
1. **NFD (Normalization Form Decomposition)**: 이 형태는 문자를 기본 구성 요소(베이스 문자와 결합 문자)로 분해합니다. 예를 들어, "é"는 "e"와 결합된 악센트로 분해됩니다.
2. **NFC (Normalization Form Composition)**: NFD로 분해된 문자를 가능한 한 다시 조합합니다. 예를 들어, "e"와 그 위의 악센트는 다시 "é"로 조합됩니다. NFC는 웹과 다른 많은 애플리케이션에서 널리 사용되는 기본 형식입니다.
3. **NFKD (Normalization Form Compatibility Decomposition)**: 이 형태는 문자를 완전히 분해하고, 호환성을 위해 시각적으로 유사한 대체 문자로 대체할 수도 있습니다. 예를 들어, 리간드나 다른 특수 기호가 일반 문자로 분해될 수 있습니다.
4. **NFKC (Normalization Form Compatibility Composition)**: NFKD로 분해한 후 가능한 다시 조합합니다. 이는 NFKD의 분해를 거친 후, 문자를 다시 조합하여 보다 일반적인 형태로 표현하는 과정입니다.

---
# 정규화 결과가 같은 글자 찾기
- [Online Generator](!https://www.irongeek.com/homoglyph-attack-generator.php)
- [Unicode Normalization Table](!https://www.unicode.org/charts/normalization/)
- 코드 작성 예시
```js
function f(x){
    for(i of x)
        if(/[A-Za-z]/g.test(i) == false && 'korea_pocas'.indexOf(i.toLowerCase()) != -1)
            console.log(i);
}
f('E e È É Ê Ë é ê ë Ē ē Ĕ ĕ Ė ė Ę Ě ě Ε Е е Ꭼ Ｅ ｅ	K k Κ κ К Ꮶ ᛕ K Ｋ ｋ0 O o Ο ο О о Օ 𐐠𱠠Ｏ ｏP p Ρ ρ Р р Ꮲ Ｐ ｐS s Ѕ ѕ Տ Ⴝ Ꮪ 𐐠𵠠Ｓ ｓÄ ӒÖ Ӧ0 O o Ο ο О о Օ 𐐠𱠠Ｏ ｏ_ ＿')
```

- NFC 정규화 결과가 같은 값을 찾는 코드
``` python
import unicodedata

target_char = 'e'
print(f"Characters that normalize to '{target_char}' in NFC:")

# 유니코드 문자 범위를 정의합니다. 여기서는 BMP(Basic Multilingual Plane) 범위를 사용합니다.
for codepoint in range(0x110000):  # U+0000 to U+10FFFF
    try:
        char = chr(codepoint)
        if unicodedata.normalize('NFC', char) == target_char:
            print(f"'{char}' (U+{codepoint:04X})")
    except ValueError:
        continue

```