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
    filepath = os.path.join("../data", filename)

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
        "========================================================================================================================================="
    )


if __name__ == "__main__":
    # Request setup
    domain = "http://sugang.kyonggi.ac.kr"
    jsessionid = get_sessionid()

    session = requests.Session()
    cookies = {"JSESSIONID": jsessionid}
    session.cookies.update(cookies)

    hr()

    print("\n\n**필수 교양**")
    # Request iteration start
    for code in subject_code_GE:
        url = (
            domain
            + "/core?attribute=lectListJson&lang=ko&gyoyang_campus_cd=A1000&gyoyang_area=75&menu=2&initYn=Y&div_cd=C&_search=false&rows=-1&page=1&sidx=&sord=asc&gyoyang_gwamok="
            + code
        )

        get_json2df(url)

    hr()

    print("\n\n**전공**")
    for code in subject_code_MAJ:
        url = (
            domain
            + "/core?attribute=lectListJson&lang=ko&fake=1706544378608&menu=3&initYn=Y&div_cd=M&_search=false&nd=1706545161331&rows=-1&page=1&sidx=&sord=as&jungong_cd="
            + code
        )

        get_json2df(url)

    pd.concat(all_course_dataframes).to_csv(
        "../data/course_registration_data.csv", index=False, encoding="utf-8-sig"
    )
