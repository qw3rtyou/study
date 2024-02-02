"""
- 참고 url (gyoyang_gwamok, jungong_cd 파라미터가 주요 식별자 코드)
공학인증(특허와기술개발) - /core?attribute=lectListJson&lang=ko&fake=1706539729898&gyoyang_campus_cd=A1000&gyoyang_area=75&gyoyang_gwamok=AS287&menu=2&initYn=Y&div_cd=C&_search=false&nd=1706539805409&rows=-1&page=1&sidx=&sord=asc
공학인증(공학윤리) - /core?attribute=lectListJson&lang=ko&fake=1706539729898&gyoyang_campus_cd=A1000&gyoyang_area=75&gyoyang_gwamok=AS916&menu=2&initYn=Y&div_cd=C&_search=false&nd=1706539864672&rows=-1&page=1&sidx=&sord=asc
전공(컴퓨터공학부) - /core?attribute=lectListJson&lang=ko&fake=1706544378608&jungong_cd=85511&menu=3&initYn=Y&div_cd=M&_search=false&nd=1706545161331&rows=-1&page=1&sidx=&sord=asc
전공(AI컴퓨터공학부) - /core?attribute=lectListJson&lang=ko&fake=1706602583396&jungong_cd=0A551&menu=3&initYn=Y&div_cd=M&_search=false&nd=1706602706606&rows=-1&page=1&sidx=&sord=asc

- Dependency
pip install pandas numpy requests tabulate
"""

import requests
import pandas as pd
import numpy as np
from tabulate import tabulate
import os
from itertools import product

# Subject code list - 컴공 2, 3 학년 기준 필요한 과목만 추가하였음. 필요하다면, 교양 과목, 전공 과목에 따라 아래 리스트에 코드 추가
subject_code_GE = ["AS287", "AS916"]
subject_code_MAJ = ["85511", "0A551"]

# Authenticate info - 사용자 세션 생성을 위해 입력(수강신청 사이트 계정정보)
user_id = "202015015"
user_pw = "hammer1346"

# Course wishlist - 듣고 싶은 강의 리스트 입력
wishlist = [
    "정보보호개론",
    "운영체제",
    "소프트웨어공학",
    "컴퓨터공학기초캡스톤디자인",
    "특허와기술개발",
    "공학윤리",
    "웹프로그래밍",
]

# Pandas display 설정
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

# 모든 수업이 담긴 global df
all_course_dataframes = []


def get_request(url):
    response = session.get(url)
    if "로그아웃" in response.text:
        print("로그인 에러!")
        exit()

    return response


def get_sessionid():
    session = requests.Session()
    response = session.get("http://sugang.kyonggi.ac.kr")

    login_data = {
        "lang": "ko",
        "id": user_id,
        "pwd": user_pw,
    }

    login_url = "http://sugang.kyonggi.ac.kr/login?attribute=loginChk&lang=ko"
    response = session.post(login_url, data=login_data)
    sessionid = session.cookies.get_dict()["JSESSIONID"]

    filename = "JSESSIONID"
    filepath = os.path.join("", filename)

    with open(filepath, "w") as file:
        file.write(sessionid)

    return sessionid


def get_json2df(url):
    response = get_request(url)
    data = response.json()

    df = pd.DataFrame(data["rows"])
    selected_df = df[["sigan", "gwamok_kname", "prof_name", "gwamok_no", "haknyun"]]

    # log_table(df, code)  # 전체 테이블
    log_table(selected_df, code)  # 간소화된 테이블
    all_course_dataframes.append(selected_df)


def log_table(df, keyword):
    hr()
    print(keyword)
    print(tabulate(df, headers="keys", tablefmt="psql"))


def hr():
    print(
        "\n========================================================================================================================================="
    )


def find_valid_combinations(course_df, wishlist):
    grouped_courses = {course: [] for course in wishlist}

    # 구룹핑
    for course in wishlist:
        course_options = course_df[course_df["gwamok_kname"].str.contains(course)]
        grouped_courses[course] = course_options.to_dict("records")

    # 모든 조합 생성
    all_combinations = product(*grouped_courses.values())

    valid_combinations = []
    for combo in all_combinations:
        if not is_time_conflict(combo):
            valid_combinations.append(combo)

    return valid_combinations


def is_time_conflict(courses):
    time_slots = set()
    for course in courses:
        times = course["sigan"].split(",")
        for time in times:
            if time in time_slots:
                return True
            time_slots.add(time)
    return False


def calculate_free_days(combo):
    weekdays = {"월", "화", "수", "목", "금"}
    for course in combo:
        course_days = set(course["sigan"].split(" ")[0])
        weekdays -= course_days
    return weekdays


def prioritize_combinations(combos):
    return sorted(combos, key=lambda x: len(calculate_free_days(x)), reverse=True)


def save_to_csv(combo, filename):
    combo_df = pd.DataFrame(combo)
    combo_df.to_csv(filename, index=False, encoding="utf-8-sig")


def register_course(session, course_code, course_name):
    course_code = str(course_code).zfill(4)

    # 수강신청에 필요한 데이터 설정
    data = {
        "params": f"01@{course_code}@00000@1",
        "retake_yn": "N",
    }

    # 수강신청 URL
    url = "http://sugang.kyonggi.ac.kr/basket?attribute=basketMode&lang=ko&fake=1706825973529&mode=insert&fake=1706825993117"

    # 수강신청 요청 보내기
    response = session.post(url, data=data, headers=headers)
    # 과목 이름과 과목 코드를 결과와 함께 출력
    return f"{course_name}({course_code}){response.text}"


if __name__ == "__main__":
    # Requests 설정
    domain = "http://sugang.kyonggi.ac.kr"
    jsessionid = get_sessionid()

    session = requests.Session()
    cookies = {"JSESSIONID": jsessionid}
    session.cookies.update(cookies)

    hr()

    while True:
        print("1. 연결된 세션값 출력")
        print("2. 전체 과목 데이터 가져오기")
        print("3. 시간표 결정")
        print("4. 소망가방신청")
        print("5. 수강신청")
        print("0. 종료")

        select = int(input("입력 : "))
        hr()

        if select == 1:
            print("sessionid : " + jsessionid)

        elif select == 2:
            # 필요한 모든 교양 정보 출력
            print("\n\n**필수 교양**")
            for code in subject_code_GE:
                url = (
                    domain
                    + "/core?attribute=lectListJson&lang=ko&gyoyang_campus_cd=A1000&gyoyang_area=75&menu=2&initYn=Y&div_cd=C&_search=false&rows=-1&page=1&sidx=&sord=asc&gyoyang_gwamok="
                    + code
                )

                get_json2df(url)

            hr()

            # 필요한 모든 전공 정보 출력
            print("\n\n**전공**")
            for code in subject_code_MAJ:
                url = (
                    domain
                    + "/core?attribute=lectListJson&lang=ko&fake=1706544378608&menu=3&initYn=Y&div_cd=M&_search=false&nd=1706545161331&rows=-1&page=1&sidx=&sord=as&jungong_cd="
                    + code
                )

                get_json2df(url)

            pd.concat(all_course_dataframes).to_csv(
                "full_data.csv", index=False, encoding="utf-8-sig"
            )

            hr()

        elif select == 3:
            # 좋은 시간표 찾는 알고리즘
            try:
                course_df = pd.read_csv("full_data.csv")
            except:
                print("먼저 전체 수강 데이터를 가져와 주세요!")
                continue
            valid_combinations = find_valid_combinations(course_df, wishlist)
            prioritized_combinations = prioritize_combinations(valid_combinations)

            hr()

            # 공강 횟수 기준 우선순위 조합 출력
            cur = 0
            while True:
                for i, combo in enumerate(prioritized_combinations[cur : cur + 10]):
                    free_days = calculate_free_days(combo)
                    print(
                        f"우선순위 조합 {i+cur+1} (공강 요일: {', '.join(free_days if free_days else ['없음'])}):"
                    )
                    for course in combo:
                        print(
                            f"- {course['gwamok_kname']} ({course['sigan']}) ({course['gwamok_no']})"
                        )
                    print("---")

                select = input("더보기(y/n)")

                if select == "y" or select == "Y" or select == "yes":
                    cur += 10
                elif select == "n" or select == "N" or select == "no":
                    break
                else:
                    cur += 10

            selected_combination = int(input("조합 선택(1~n) : "))

            # 선택한 조합 csv로 저장
            if prioritized_combinations:
                save_to_csv(
                    prioritized_combinations[selected_combination - 1],
                    "target_data.csv",
                )

            hr()

        elif select == 4:
            # JSESSIONID 읽기
            with open("JSESSIONID", "r") as file:
                jsessionid = file.read().strip()

            # 세션 설정 및 쿠키 업데이트
            session = requests.Session()
            cookies = {"JSESSIONID": jsessionid}
            session.cookies.update(cookies)

            # HTTP 요청 헤더 설정
            headers = {
                "Accept": "*/*",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "http://sugang.kyonggi.ac.kr",
                "Referer": "http://sugang.kyonggi.ac.kr/core?attribute=coreMain_ko&fake=Fri%20Feb%2002%2007:19:26%20KST%202024",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            }

            # target_schedule.csv 파일 읽기
            try:
                schedule_df = pd.read_csv("target_data.csv")
            except:
                print("먼저 수강신청할 시간표를 결정해주세요!")

            # 각 과목에 대해 수강신청 진행
            for _, row in schedule_df.iterrows():
                course_code = row["gwamok_no"]
                course_name = row["gwamok_kname"]
                response_text = register_course(session, course_code, course_name)
                print(f"{response_text}\n")

            hr()

        elif select == 5:
            print("제작중..")
            hr()

        elif select == 0:
            exit()

        else:
            continue
