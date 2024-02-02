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


if __name__ == "__main__":
    course_df = pd.read_csv("../data/course_registration_data.csv")
    valid_combinations = find_valid_combinations(course_df, wishlist)

    for i, combo in enumerate(valid_combinations, 1):
        print(f"조합 {i}:")
        for course in combo:
            print(
                f"- {course['gwamok_kname']} ({course['sigan']}) ({course['gwamok_no']})"
            )
        print("---")
