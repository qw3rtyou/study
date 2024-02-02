import pandas as pd
from itertools import product

# Pandas display setup
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

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
    course_df = pd.read_csv("../data/course_registration_data.csv")
    valid_combinations = find_valid_combinations(course_df, wishlist)
    prioritized_combinations = prioritize_combinations(valid_combinations)

    # 상위 조합 출력
    for i, combo in enumerate(prioritized_combinations[:54], 1):
        free_days = calculate_free_days(combo)
        print(
            f"우선순위 조합 {i} (수업 없는 요일: {', '.join(free_days if free_days else ['없음'])}):"
        )
        for course in combo:
            print(
                f"- {course['gwamok_kname']} ({course['sigan']}) ({course['gwamok_no']})"
            )
        print("---")

    # 우선순위 조합 1 csv로 저장
    if prioritized_combinations:
        save_to_csv(prioritized_combinations[18], "../data/target_schedule.csv")
