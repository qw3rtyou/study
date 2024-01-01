파일 복제

```python
import shutil

with open("data/shutil_ex.txt",'w') as file:
	file.write("hello shutil!\nshutil is shell+utill")

shutil.copy("data/shutil_ex.txt","data/shutil_ex2.txt")

```
