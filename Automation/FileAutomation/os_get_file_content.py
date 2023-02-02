file=open("os_check_file_5mb.py",encoding='UTF-8')
#파이썬은 기본적으로 인코딩을 ANSI로 함
#파일을 ANSI로 인코딩해주거나
#위에처럼 인코딩을 따로 지정해줘야함

print(file.readline())
print(file.readline())

file.seek(0)    #파일 커서 처음으로 옮기기
print(file.read())

file.seek(0)    #파일 커서 처음으로 옮기기
print(file.readlines())

file.close()