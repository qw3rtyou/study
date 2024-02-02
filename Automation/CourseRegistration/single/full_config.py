# 공학인증(특허와기술개발) - /core?attribute=lectListJson&lang=ko&fake=1706539729898&gyoyang_campus_cd=A1000&gyoyang_area=75&gyoyang_gwamok=AS287&menu=2&initYn=Y&div_cd=C&_search=false&nd=1706539805409&rows=-1&page=1&sidx=&sord=asc
# 공학인증(공학윤리) - /core?attribute=lectListJson&lang=ko&fake=1706539729898&gyoyang_campus_cd=A1000&gyoyang_area=75&gyoyang_gwamok=AS916&menu=2&initYn=Y&div_cd=C&_search=false&nd=1706539864672&rows=-1&page=1&sidx=&sord=asc
# 전공(컴퓨터공학부) - /core?attribute=lectListJson&lang=ko&fake=1706544378608&jungong_cd=85511&menu=3&initYn=Y&div_cd=M&_search=false&nd=1706545161331&rows=-1&page=1&sidx=&sord=asc
# 전공(AI컴퓨터공학부) - /core?attribute=lectListJson&lang=ko&fake=1706602583396&jungong_cd=0A551&menu=3&initYn=Y&div_cd=M&_search=false&nd=1706602706606&rows=-1&page=1&sidx=&sord=asc

# pip install pandas numpy requests tabulate

import requests
import pandas as pd
import numpy as np
from tabulate import tabulate
import os
from itertools import product

# Subject code list
subject_code_GE = ["AS287", "AS916"]
subject_code_MAJ = ["85511", "0A551"]

# Pandas display setup
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

# Authenticate info
user_id = "202015015"
user_pw = "hammer1346"

# Course wishlist
wishlist = [
    "정보보호개론",
    "운영체제",
    "소프트웨어공학",
    "컴퓨터공학기초캡스톤디자인",
    "특허와기술개발",
    "공학윤리",
    "웹프로그래밍",
]

# Global Dataframe for all course
all_course_dataframes = []


def get_request(url):
    response = session.get(url)
    if "로그아웃" in response.text:
        print("session error!")
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

    print("sessionid : " + session.cookies.get_dict()["JSESSIONID"])

    filename = "JSESSIONID"
    filepath = os.path.join("", filename)

    with open(filepath, "w") as file:
        file.write(sessionid)

    return sessionid


def get_json2df(url):
    # Request start
    response = get_request(url)
    data = response.json()

    # filter Dataframe, print and save
    df = pd.DataFrame(data["rows"])
    selected_df = df[["sigan", "gwamok_kname", "prof_name", "gwamok_no", "haknyun"]]

    log_table(df, code)  # full table
    # log_table(selected_df, code)
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

    # Grouping
    for course in wishlist:
        course_options = course_df[course_df["gwamok_kname"].str.contains(course)]
        grouped_courses[course] = course_options.to_dict("records")

    # Generate all combination
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


if __name__ == "__main__":
    # Requests 설정
    domain = "http://sugang.kyonggi.ac.kr"
    jsessionid = get_sessionid()

    session = requests.Session()
    cookies = {"JSESSIONID": jsessionid}
    session.cookies.update(cookies)

    hr()

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
        "course_registration_data.csv", index=False, encoding="utf-8-sig"
    )

    hr()

    # 좋은 시간표 찾는 알고리즘
    course_df = pd.read_csv("course_registration_data.csv")
    valid_combinations = find_valid_combinations(course_df, wishlist)
    prioritized_combinations = prioritize_combinations(valid_combinations)

    hr()

    # 공강 횟수 기준 우선순위 조합 출력
    try:
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

    except:
        print("모든 조합 출력됨")

    finally:
        selected_combination = int(input("조합 선택(1~n) : "))

    # 선택한 조합 csv로 저장
    if prioritized_combinations:
        save_to_csv(
            prioritized_combinations[selected_combination - 1],
            "target_schedule.csv",
        )
