
# Trial

- `2-letter combinations` 이랑 `3-letter combinations` 중에 어떤 걸 사용할 지 결정해야 했는데,  [Trigram 파일](https://github.com/David-Hinschberger/Monoalphabetic-Cipher-Decoder/commit/2096c3f5f2da7b96d69917c864941deb0e969486)에서 헤당 데이터를 얻을 수 있어서 `3-letter combinations`으로 결정
- 처음에는 `Bruteforce` 방식으로 모든 방법을 시도한 후 평가를 하게 설계하였지만, 너무 오래걸림
- 찾아보니 유전 알고리즘을 통해 해결할 수 있었음

---
# Encrypt Text

- 대소문자 구분이 없지만, 띄어쓰기, 문장 기호 등이 들어가 있는 대체 암호화 방식이 암호문
``` plain
APS ZU BMS THAAMT KB SOP CHAAPJ MQ LPUWHKX. K UHJ SM JMZ SMLHJ VJ QXKPBLU -- UM PCPB SOMZDO TP QHEP SOP LKQQKEZASKPU MQ SMLHJ HBL SMVMXXMT, K USKAA OHCP H LXPHV. KS KU H LXPHV LPPWAJ XMMSPL KB SOP HVPXKEHB LXPHV. K OHCP H LXPHV SOHS MBP LHJ SOKU BHSKMB TKAA XKUP ZW HBL AKCP MZS SOP SXZP VPHBKBD MQ KSU EXPPL: "TP OMAL SOPUP SXZSOU SM IP UPAQ-PCKLPBS, SOHS HAA VPB HXP EXPHSPL PGZHA." K OHCP H LXPHV SOHS MBP LHJ MB SOP XPL OKAAU MQ DPMXDKH SOP UMBU MQ QMXVPX UAHCPU HBL SOP UMBU MQ QMXVPX UAHCP MTBPXU TKAA IP HIAP SM UKS LMTB SMDPSOPX HS SOP SHIAP MQ IXMSOPXOMML. K OHCP H LXPHV SOHS MBP LHJ PCPB SOP USHSP MQ VKUUKUUKWWK, H USHSP UTPASPXKBD TKSO SOP OPHS MQ KBFZUSKEP, UTPASPXKBD TKSO SOP OPHS MQ MWWXPUUKMB, TKAA IP SXHBUQMXVPL KBSM HB MHUKU MQ QXPPLMV HBL FZUSKEP. K OHCP H LXPHV SOHS VJ QMZX AKSSAP EOKALXPB TKAA MBP LHJ AKCP KB H BHSKMB TOPXP SOPJ TKAA BMS IP FZLDPL IJ SOP EMAMX MQ SOPKX URKB IZS IJ SOP EMBSPBS MQ SOPKX EOHXHESPX. K OHCP H LXPHV SMLHJ. K OHCP H LXPHV SOHS MBP LHJ LMTB KB HAHIHVH, TKSO KSU CKEKMZU XHEKUSU, TKSO KSU DMCPXBMX OHCKBD OKU AKWU LXKWWKBD TKSO SOP TMXLU MQ KBSPXWMUKSKMB HBL BZAAKQKEHSKMB -- MBP LHJ XKDOS SOPXP KB HAHIHVH AKSSAP IAHER IMJU HBL IAHER DKXAU TKAA IP HIAP SM FMKB OHBLU TKSO AKSSAP TOKSP IMJU HBL TOKSP DKXAU HU UKUSPXU HBL IXMSOPXU. K OHCP H LXPHV SMLHJ. K OHCP H LXPHV SOHS MBP LHJ PCPXJ CHAAPJ UOHAA IP PNHASPL, HBL PCPXJ OKAA HBL VMZBSHKB UOHAA IP VHLP AMT, SOP XMZDO WAHEPU TKAA IP VHLP WAHKB, HBL SOP EXMMRPL WAHEPU TKAA IP VHLP USXHKDOS, HBL SOP DAMXJ MQ SOP AMXL UOHAA IP XPCPHAPL HBL HAA QAPUO UOHAA UPP KS SMDPSOPX.
```


---
# Decryption

- 램덤하게 키를 생성하고, 각 후보 키들이 세대를 거듭하여 최적의 해를 찾아가는 방식
- 각 글자 빈도 수 테이블을 출력해주지만 `3-letter combinations` 방식이므로 이 코드에서는 크게 의미는 없음
- 추가적으로 결과 key 테이블과 복호화 결과를 출력해줌
``` python
import random
from ratings import TRIGRAM_RATINGS

NUM_HILLS = 50
STEPS_PER_HILL = 5000

def calculate_frequency_table(ciphertext):
    frequency = {}
    for char in ciphertext:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

def print_frequency_table(frequency):
    print("1. Frequency count Table")
    for char, freq in sorted(frequency.items()):
        print(f"{char}: {freq}")
    print("======================")

def print_key_table(key):
    print("2. Key table:")
    for i, cipher_char in enumerate(key):
        print(f"{cipher_char} -> {chr(i + 65)}")
    print("======================")
    
def decrypt_with_key(ciphertext, key):
    for i, cipher_char in enumerate(key):
        plaintext_char = chr(i + 65)
        ciphertext = ciphertext.replace(cipher_char, plaintext_char.lower())
    return ciphertext.upper()

def calculate_rating(text):
    rating = 0
    for i in range(3, len(text)):
        trigram = text[i - 3:i]
        rating += TRIGRAM_RATINGS.get(trigram, 0)
    return rating

def generate_initial_key():
    return random.sample(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 26)

def mutate_key(key):
    idx1, idx2 = random.sample(range(26), 2)
    key[idx1], key[idx2] = key[idx2], key[idx1]
    return key

def find_best_key(ciphertext):
    best_key, best_rating = None, 0

    for _ in range(NUM_HILLS):
        current_key = generate_initial_key()
        current_rating = calculate_rating(decrypt_with_key(ciphertext, current_key))

        for _ in range(STEPS_PER_HILL):
            new_key = mutate_key(current_key.copy())
            new_rating = calculate_rating(decrypt_with_key(ciphertext, new_key))
            if new_rating > current_rating:
                current_key, current_rating = new_key, new_rating

        if current_rating > best_rating:
            best_key, best_rating = current_key, current_rating

    return best_key, best_rating

def main():
    with open("input.txt", "r") as file:
        ciphertext = file.read()

    frequency = calculate_frequency_table(ciphertext)
    print_frequency_table(frequency)

    best_key, best_rating = find_best_key(ciphertext)
    decrypted_text = decrypt_with_key(ciphertext, best_key)

    print(f"Best key found: {''.join(best_key)}, rating: {best_rating}")
    print_key_table(best_key)
    
    print(f"3. Plaintext decrypted:\n{decrypted_text}")

if __name__ == "__main__":
    main()
```


---
# Solution

- 실행결과
```plain
$ python3 Decipher.py 
====================
1. Frequency count Table
A: 81
B: 68
C: 24
D: 18
E: 20
F: 4
G: 1
H: 124
I: 24
J: 26
K: 97
L: 63
M: 87
N: 1
O: 75
P: 156
Q: 27
R: 4
S: 116
T: 29
U: 68
V: 28
W: 14
X: 69
Z: 18

======================
Best key found: HIELPQDOKFRAVBMWGXUSZCTNJY, rating: 1.2283482735612266

======================
2. Key table:
H -> A
I -> B
E -> C
L -> D
P -> E
Q -> F
D -> G
O -> H
K -> I
F -> J
R -> K
A -> L
V -> M
B -> N
M -> O
W -> P
G -> Q
X -> R
U -> S
S -> T
Z -> U
C -> V
T -> W
N -> X
J -> Y
Y -> Z

======================
3. Plaintext decrypted:
LET US NOT WALLOW IN THE VALLEY OF DESPAIR. I SAY TO YOU TODAY MY FRIENDS -- SO EVEN THOUGH WE
FACE THE DIFFICULTIES OF TODAY AND TOMORROW, I STILL HAVE A DREAM. IT IS A DREAM DEEPLY ROOTED
IN THE AMERICAN DREAM. I HAVE A DREAM THAT ONE DAY THIS NATION WILL RISE UP AND LIVE OUT THE TRUE
MEANING OF ITS CREED: "WE HOLD THESE TRUTHS TO BE SELF-EVIDENT, THAT ALL MEN ARE CREATED EQUAL."
I HAVE A DREAM THAT ONE DAY ON THE RED HILLS OF GEORGIA THE SONS OF FORMER SLAVES AND THE SONS
OF FORMER SLAVE OWNERS WILL BE ABLE TO SIT DOWN TOGETHER AT THE TABLE OF BROTHERHOOD. I HAVE A
DREAM THAT ONE DAY EVEN THE STATE OF MISSISSIPPI, A STATE SWELTERING WITH THE HEAT OF INJUSTICE,
SWELTERING WITH THE HEAT OF OPPRESSION, WILL BE TRANSFORMED INTO AN OASIS OF FREEDOM AND
JUSTICE. I HAVE A DREAM THAT MY FOUR LITTLE CHILDREN WILL ONE DAY LIVE IN A NATION WHERE THEY WILL
NOT BE JUDGED BY THE COLOR OF THEIR SKIN BUT BY THE CONTENT OF THEIR CHARACTER. I HAVE A DREAM
TODAY. I HAVE A DREAM THAT ONE DAY DOWN IN ALABAMA, WITH ITS VICIOUS RACISTS, WITH ITS GOVERNOR
HAVING HIS LIPS DRIPPING WITH THE WORDS OF INTERPOSITION AND NULLIFICATION -- ONE DAY RIGHT
THERE IN ALABAMA LITTLE BLACK BOYS AND BLACK GIRLS WILL BE ABLE TO JOIN HANDS WITH LITTLE WHITE
BOYS AND WHITE GIRLS AS SISTERS AND BROTHERS. I HAVE A DREAM TODAY. I HAVE A DREAM THAT ONE DAY
EVERY VALLEY SHALL BE EXALTED, AND EVERY HILL AND MOUNTAIN SHALL BE MADE LOW, THE ROUGH PLACES
WILL BE MADE PLAIN, AND THE CROOKED PLACES WILL BE MADE STRAIGHT, AND THE GLORY OF THE LORD
SHALL BE REVEALED AND ALL FLESH SHALL SEE IT TOGETHER.
```

- 복호화문
```
LET US NOT WALLOW IN THE VALLEY OF DESPAIR. I SAY TO YOU TODAY MY FRIENDS -- SO EVEN THOUGH WE
FACE THE DIFFICULTIES OF TODAY AND TOMORROW, I STILL HAVE A DREAM. IT IS A DREAM DEEPLY ROOTED
IN THE AMERICAN DREAM. I HAVE A DREAM THAT ONE DAY THIS NATION WILL RISE UP AND LIVE OUT THE TRUE
MEANING OF ITS CREED: "WE HOLD THESE TRUTHS TO BE SELF-EVIDENT, THAT ALL MEN ARE CREATED EQUAL."
I HAVE A DREAM THAT ONE DAY ON THE RED HILLS OF GEORGIA THE SONS OF FORMER SLAVES AND THE SONS
OF FORMER SLAVE OWNERS WILL BE ABLE TO SIT DOWN TOGETHER AT THE TABLE OF BROTHERHOOD. I HAVE A
DREAM THAT ONE DAY EVEN THE STATE OF MISSISSIPPI, A STATE SWELTERING WITH THE HEAT OF INJUSTICE,
SWELTERING WITH THE HEAT OF OPPRESSION, WILL BE TRANSFORMED INTO AN OASIS OF FREEDOM AND
JUSTICE. I HAVE A DREAM THAT MY FOUR LITTLE CHILDREN WILL ONE DAY LIVE IN A NATION WHERE THEY WILL
NOT BE JUDGED BY THE COLOR OF THEIR SKIN BUT BY THE CONTENT OF THEIR CHARACTER. I HAVE A DREAM
TODAY. I HAVE A DREAM THAT ONE DAY DOWN IN ALABAMA, WITH ITS VICIOUS RACISTS, WITH ITS GOVERNOR
HAVING HIS LIPS DRIPPING WITH THE WORDS OF INTERPOSITION AND NULLIFICATION -- ONE DAY RIGHT
THERE IN ALABAMA LITTLE BLACK BOYS AND BLACK GIRLS WILL BE ABLE TO JOIN HANDS WITH LITTLE WHITE
BOYS AND WHITE GIRLS AS SISTERS AND BROTHERS. I HAVE A DREAM TODAY. I HAVE A DREAM THAT ONE DAY
EVERY VALLEY SHALL BE EXALTED, AND EVERY HILL AND MOUNTAIN SHALL BE MADE LOW, THE ROUGH PLACES
WILL BE MADE PLAIN, AND THE CROOKED PLACES WILL BE MADE STRAIGHT, AND THE GLORY OF THE LORD
SHALL BE REVEALED AND ALL FLESH SHALL SEE IT TOGETHER.
```
