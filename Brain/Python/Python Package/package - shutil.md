---
sticker: lucide//file
---
# shutil
-  파일 및 디렉토리 관리 자겅ㅂ을 위한 여러 유용한 함수 제공
- shell utilities

파일 복제

```python
import shutil

with open("data/shutil_ex.txt",'w') as file:
	file.write("hello shutil!\nshutil is shell+utill")

shutil.copy("data/shutil_ex.txt","data/shutil_ex2.txt")

```


- 디렉터리 재귀적으로 복사
```python
import shutil 

shutil.copytree('source_directory', 'destination_directory')
```


- 디렉터리 삭제
```python
import shutil  
shutil.rmtree('directory_to_delete')
```


- 디스크 사용량 조회
```python
import shutil  
total, used, free = shutil.disk_usage('.') 
print(f"Total: {total}, Used: {used}, Free: {free}")
```