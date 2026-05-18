import pandas as pd
 # User Interaction Testing 
 # any input tissues would be here 
scholarships = pd.read_csv("scholarships.csv")


student_name = input("Enter your name: ")
student_gpa = float(input("Enter your GPA: "))
student_major = input("Enter your major: ")
student_state = input("Enter your state of residence: ")
student_first_gen = input("Are you a first-generation college student? (yes/no): ")
student_financial_need = input("Do you have financial need? (Yes/No): ")

gpa_condition = scholarships["min_gpa"] <= student_gpa

major_condition = (
    (scholarships["major"] == student_major) |
    (scholarships["major"] == "Any")
)

state_condition = (
    (scholarships["state"] == student_state) |
    (scholarships["state"] == "Any")
)

first_generation = (
    (scholarships["first_gen_required"] == student_first_gen) |
    (scholarships["first_gen_required"] == "No")
    )
   

financial_need_condition = (
    (scholarships["financial_need_required"] == student_financial_need) |
    (scholarships["financial_need_required"] == "No")
)
matches = scholarships[
    gpa_condition &
    major_condition &
    state_condition &
    first_generation &
    financial_need_condition 
]

print(f"\nScholarships for {student_name}:\n")

if matches.empty:
    print("No matching scholarships found.")
else:
    print(matches[["name", "amount", "deadline", "min_gpa", "major", "state"]])