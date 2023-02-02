import os
import datetime

path = 'os_print_os_name.py'

# 타임스탬프 형식의 생성 시간
# 예시: 1594616754.1851065
creation_time = os.path.getctime(path)
modify_time = os.path.getmtime(path)
access_time = os.path.getatime(path)

# datetime 모듈을 사용해서 보기 좋게 변경하기
# 예시: 2020-06-19 14:26:52.981000
format_creation_time = datetime.datetime.fromtimestamp(creation_time)
format_modify_time = datetime.datetime.fromtimestamp(modify_time)
format_access_time = datetime.datetime.fromtimestamp(access_time)

# 문자열과 함께 출력하고 싶다면 format을 사용
print("{} 생성 시각: {}".format(path,format_creation_time))
print("{} 수정 시각: {}".format(path,format_modify_time))
print("{} 참조 시각: {}".format(path,format_access_time))