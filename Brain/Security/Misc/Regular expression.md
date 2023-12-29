# 정의
정규 표현식(Regular Expression)은 특정한 패턴으로 문자열을 표현하는 식
일반적으로 문자열 내에서 원하는 패턴의 문자열을 찾거나 치환할 때 사용
‘패턴’은 어떤 문자 조합을 식으로 나타낸 것을 의미
정규 표현식에 부합하는 문자열의 경우, 정규 표현식 혹은 패턴에 ‘매치한다’고 표현



# 정규 표현식 패턴
정규 표현식은 `'패턴'` 혹은 `/패턴/` 의 형태로 작성
`/`로 패턴을 감싸는 경우, `/` 뒤에 플래그를 작성할 수 있음

### 매치

|**패턴**|**설명**|**예시**|
|---|---|---|
|문자 혹은 문자열|해당 문자 혹은 문자열과 매치합니다.|dreamhack → Hello **dreamhack**<br><br>/c/ → Hello dreamha**c**k|
|.|모든 문자와 매치합니다.|d.eamhack → Hello **dxeamhack**|
|\||앞 또는 뒤의 패턴과 매치합니다.|hi\|dream → Hello **dream**hack|
|[ ]|[ ] 안의 문자와 매치합니다.|[aeiou] → H**i**|
|[^ ]|^ 뒤의 패턴을 제외한 나머지와 매치합니다.|[^aeiou] → **H**i|
|^|어떤 문자열의 시작이 특정 패턴인 경우 매치합니다.|^dream → **dream**hack Hello<br><br>^dream → Hello dreamhack|
|$|어떤 문자열의 끝이 특정 패턴인 경우 매치합니다.|hack$ → dreamhack Hello<br><br>hack$ → Hello dream**hack**|
|\|\ 뒤의 특수 문자와 매치합니다.<br><br>특별한 목적으로 사용되는 특수 문자를 문자 그대로 쓰기 위한 이스케이핑입니다.|hack\$ → Hello dream**hack$**|
|[a-z]<br><br>[A-Z]<br><br>[0-9]|두 문자 사이 범위의 문자와 매치합니다.|[b-d] → ha**c**k|
|\w|알파벳 또는 숫자 또는 `_`와 매치합니다.<br><br>[A-Za-z0-9_]|\w → **a**!|
|\d|숫자와 매치합니다.<br><br>[0-9]|\d → a**1**|
|\s|공백 문자와 매치합니다.<br><br>[\b\f\n\r\t\v]|   |


### 수량자


<table><colgroup><col style="width: 35.6%"><col style="width: 32.2%"><col style="width: 32.2%"></colgroup><tbody><tr><th><p><strong>패턴</strong></p></th><th><p><strong>설명</strong></p></th><th><p><strong>예시</strong></p></th></tr><tr><td><p>*</p></td><td><p>앞에 나온 문자가 0개 이상이면 매치합니다.</p></td><td><p>Hac*k → <strong><span style="color: rgb(101,84,192);">Hak</span></strong></p><p>Hac*k → <strong><span style="color: rgb(101,84,192);">Hack</span></strong></p></td></tr><tr><td><p>+</p></td><td><p>앞에 나온 문자가 1개 이상이면 매치합니다.</p></td><td><p>Hac+k → Hak</p><p>Hac+k → <strong><span style="color: rgb(101,84,192);">Hack</span></strong></p></td></tr><tr><td><p>?</p></td><td><p>앞에 나온 문자 0개 혹은 1개이면 매치합니다.</p></td><td><p>Hac?k → <strong><span style="color: rgb(101,84,192);">Hak</span></strong></p><p>Hac?k → <strong><span style="color: rgb(101,84,192);">Hack</span></strong></p></td></tr><tr><td><p>수량자?</p></td><td><p>수량자 뒤에 ?를 붙이면 게으른 수량자로, 최소한의 문자만 매치합니다.</p></td><td><p>&lt;p&gt;.*&lt;/p&gt; → <strong><span style="color: rgb(101,84,192);">&lt;p&gt;Hello&lt;/p&gt;&lt;p&gt;Hi&lt;/p&gt;</span></strong></p><p>&lt;p&gt;.*?&lt;/p&gt; → <strong><span style="color: rgb(101,84,192);">&lt;p&gt;Hello&lt;/p&gt;</span></strong>&lt;p&gt;Hi&lt;/p&gt;</p><p>Hack+? → <strong><span style="color: rgb(101,84,192);">Hack</span></strong></p><p>Hack+? → Hackk</p></td></tr><tr><td><p>{n}</p></td><td><p>앞에 나온 문자가 정확히 n개이면 매치합니다.</p></td><td><p>Hac{3}k → <strong><span style="color: rgb(101,84,192);">Haccck</span></strong></p></td></tr><tr><td><p>{n, }</p></td><td><p>앞에 나온 문자가 n개 이상이면 매치합니다.</p></td><td><p>Hac{2,}k → <strong><span style="color: rgb(101,84,192);">Haccck</span></strong></p></td></tr><tr><td><p>{n1, n2}</p></td><td><p>앞에 나온 문자가 n1개 이상, n2개 이하면 매치합니다.</p></td><td><p>Hac{2,3}k → <strong><span style="color: rgb(101,84,192);">Hacck</span></strong></p><p>Hac{2,3}k → <strong><span style="color: rgb(101,84,192);">Haccck</span></strong></p></td></tr></tbody></table>


### 그룹화

|**패턴**|**설명**|**예시**|
|---|---|---|
|( )|( )로 감싼 부분을 그룹화하여 하나의 문자처럼 여깁니다.|(ha)+ck → **hahahack**|



# 정규표현식 플래그

|**플래그**|**설명**|**예시**|
|---|---|---|
|g|**g**lobal search<br><br>매치하는 모든 문자/문자열을 검색합니다.|/[aeiou]/ → H**e**llo dreamhack<br><br>/[aeiou]/g → H**e**ll**o** dr**ea**mh**a**ck|
|i|**i**gnore case<br><br>대소문자를 구분하지 않고 검색합니다.|/h/g → Hello dream**h**ack<br><br>/h/ig → **H**ello dream**h**ack|
|m|**m**ultiline<br><br>여러 줄에서 검색합니다.|/^Hello/g → **Hello** dream<br><br>Hello hack<br><br>/^Hello/gm → **Hello** dream<br><br>**Hello** hack|
|s|**s**ingle line(dotall)<br><br>메타문자 `.`가 개행문자도 포함합니다.|/Hello.+hack/g → Hello dream<br><br>**Hello hack**<br><br>/Hello.+hack/s → **Hello dream**<br><br>**Hello hack**|



# 파이썬으로 정규표현식 사용하기
Python에서는 `re` 모듈을 통해 정규 표현식을 사용할 수 있음


|**함수**|**설명**|**반환 값**|
|---|---|---|
|`re.compile(pattern, flags)`|정규 표현식 패턴을 컴파일합니다.|패턴 객체를 반환합니다. 만들어진 패턴 객체는 변수에 저장하여 사용할 수 있습니다.|
|`re.search(pattern, string, flags)`|문자열 내에서 패턴에 처음으로 매치하는 문자열을 검색합니다.|매치하는 문자열이 있으면 문자열 객체를 반환하고, 없으면 None을 반환합니다.<br><br>문자열 객체의 `group()` 메소드를 사용하여 객체에서 문자열만 반환할 수 있습니다.|
|`re.match(pattern, string, flags)`|문자열 시작 부분에서 패턴에 매치하는 문자열을 검색합니다.|
|`re.fullmatch(pattern, string, flags)`|전체 문자열이 패턴과 정확하게 매치하는지 확인합니다.|
|`re.findall(pattern, string, flags)`|문자열 내에서 패턴에 매치하는 모든 문자열을 검색합니다.|모든 문자열을 리스트 형식으로 반환합니다. 각 문자열은 리스트의 인덱스로 접근합니다.|
|`re.finditer(pattern, string, flags)`|모든 문자열 객체를 리스트 형식으로 반환합니다.|


## flags

Python에서 정규 표현식 플래그는 함수의 `flags` 인자 값으로 지정하거나, 패턴에 인라인 형식으로 작성

|**플래그**|**flags 인자 값**|**인라인 플래그**|
|---|---|---|
|i|re.I (re.IGNORECASE)|(?i)|
|m|re.M (re.MULTILINE)|(?m)|
|s|re.S (re.DOTALL)|(?s)|
|g|자동으로 적용됩니다.|   |


## Raw String (r-string)
Raw String은 문자열 앞에 'r'을 붙여 나타냄
Raw String은 이스케이프 문자를 문자 그대로 인식하는 특수한 문자열


```python
print('\t'+'Hi')
# 결과: Hi 
# Raw String
print(r'\t'+'Hi')
# 결과: \tHi
```


##### 대문자만 출력하기
```python
import re result = re.findall('[A-Z]', 'Hello, DreamHack!') 
#same
pattern = re.compile('[A-Z]')
result = pattern.findall('Hello, DreamHack!') 
print(result) 
# 결과: ['H', 'D', 'H']
```


# JavaScript으로 정규표현식 사용하기
JavaScript에서는 2가지 방법으로 정규 표현식을 사용할 수 있음

첫 번째 방법은 정규 표현식 리터럴을 사용하는 것
`/패턴/` 혹은 `/패턴/플래그`의 형태로 작성

두 번째 방법은 RegExp 객체를 생성하는 것
`new RegExp(정규 표현식 리터럴, '플래그')` 혹은 `new RegExp('패턴', '플래그')`로 객체를 생성

|**함수**|**설명**|
|---|---|
|`pattern.exec(string)`|패턴에 처음으로 매치하는 문자열의 일치 정보를 나타내는 결과 배열을 반환합니다.|
|`pattern.test(string)`|패턴에 매치하는 부분이 있으면 true, 없으면 false를 반환합니다.|
|`string.match(pattern)`|패턴에 매치하는 모든 문자열을 배열 형태로 반환합니다.|


##### 전체 문자열에서 숫자만 출력하기
```js
const r = /\d/g;
// same
// const r = new RegExp('\\d','g');
// const r = new RegExp(/\d/,'g'); 

const str = 'H3ll0, DreamH4ck!';
const result = str.match(r);
console.log(result); 
// 결과: ['3', '0', '4']
```



# 주요사이트
정규표현식 시각화
https://regexper.com/

실시간 패턴 매치 결과 제공 + 해석
https://regexr.com/

































