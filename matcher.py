import pandas as pd
import pandas as pd


def find_matches(
    student_gpa,
    student_major,
    student_state,
    student_first_gen,
    student_financial_need,
):
    scholarships = pd.read_csv("scholarships.csv")

    results = []

    # Clean the student's text once before the loop.
    student_major = student_major.strip().title()
    student_state = student_state.strip().upper()

    for row_index, scholarship in scholarships.iterrows():
        scholarship_major = str(scholarship["major"]).strip().title()
        scholarship_state = str(scholarship["state"]).strip().upper()

        first_gen_required = str(
            scholarship["first_gen_required"]
        ).strip().title()

        financial_need_required = str(
            scholarship["financial_need_required"]
        ).strip().title()

        minimum_gpa = float(scholarship["min_gpa"])

        # -------------------------
        # Step 1: Eligibility checks
        # -------------------------

        if student_gpa < minimum_gpa:
            continue

        if scholarship_major != "Any" and scholarship_major != student_major:
            continue

        if scholarship_state != "ANY" and scholarship_state != student_state:
            continue

        if first_gen_required == "Yes" and student_first_gen != "Yes":
            continue

        if (
            financial_need_required == "Yes"
            and student_financial_need != "Yes"
        ):
            continue

        # -------------------------
        # Step 2: Match score
        # -------------------------

        score = 25  # Student meets the GPA requirement.

        if scholarship_major == student_major:
            score += 25
        else:
            score += 15

        if scholarship_state == student_state:
            score += 20
        else:
            score += 10

        if first_gen_required == student_first_gen:
            score += 15
        else:
            score += 10

        if financial_need_required == student_financial_need:
            score += 15
        else:
            score += 10

        scholarship_data = scholarship.to_dict()
        scholarship_data["row_index"] = row_index
        scholarship_data["match_score"] = score

        results.append(scholarship_data)

    matches = pd.DataFrame(results)

    if not matches.empty:
        matches = matches.sort_values(
            by="match_score",
            ascending=False,
        ).reset_index(drop=True)

    return matches