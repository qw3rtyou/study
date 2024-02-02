import requests
import pandas as pd


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
    return f"과목명: {course_name}, 과목 코드: {course_code}, 수강신청 결과: {response.text}"


if __name__ == "__main__":
    # JSESSIONID 읽기
    with open("../data/JSESSIONID", "r") as file:
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
    schedule_df = pd.read_csv("../data/target_schedule.csv")

    # 각 과목에 대해 수강신청 진행
    for _, row in schedule_df.iterrows():
        course_code = row["gwamok_no"]
        course_name = row["gwamok_kname"]
        response_text = register_course(session, course_code, course_name)
        print(f"{course_name}({course_code}) 수강신청 결과: {response_text}\n")
