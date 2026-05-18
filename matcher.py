import pandas as pd

def find_matches(student_gpa, student_major, student_state, student_first_gen, student_financial_need):
    scholarships = pd.read_csv("scholarships.csv")

    results = []

    for row_index, scholarship in scholarships.iterrows():
        score = 0

        # GPA match
        if student_gpa >= scholarship["min_gpa"]:
            score += 25

        # Major match
        if scholarship["major"] == student_major:
            score += 25
        elif scholarship["major"] == "Any":
            score += 15

        # State match
        if scholarship["state"] == student_state:
            score += 20
        elif scholarship["state"] == "Any":
            score += 10

        # First-generation match
        if scholarship["first_gen_required"] == student_first_gen:
            score += 15
        elif scholarship["first_gen_required"] == "No":
            score += 10

        # Financial need match
        if scholarship["financial_need_required"] == student_financial_need:
            score += 15
        elif scholarship["financial_need_required"] == "No":
            score += 10

        if score > 0:
            scholarship_data = scholarship.to_dict()
            scholarship_data["row_index"] = row_index
            scholarship_data["match_score"] = score
            results.append(scholarship_data)

    matches = pd.DataFrame(results)

    if not matches.empty:
        matches = matches.sort_values(by="match_score", ascending=False)

    return matches