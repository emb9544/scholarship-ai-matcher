import streamlit as st
from matcher import find_matches

st.set_page_config(
    page_title="Scholarship AI Matcher",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Scholarship AI Matcher")
st.write("Find scholarships that match your academic profile, background, and needs.")

with st.sidebar:
    st.header("Student Profile")

    student_name = st.text_input("Name")
    student_gpa = st.number_input("GPA", min_value=0.0, max_value=4.0, step=0.1)
    student_major = st.text_input("Major")
    student_state = st.text_input("State of residence")

    student_first_gen = st.selectbox(
        "First-generation college student?",
        ["Yes", "No"]
    )

    student_financial_need = st.selectbox(
        "Financial need?",
        ["Yes", "No"]
    )
    student_interests = st.text_area(
    "Tell us about your interests, career goals, or background"
)
    #this is where user will input what they want
    #AI will generate scholarships based on this input and the rest of the profile

    search_button = st.button("Find Scholarships")

if search_button:
    matches = find_matches(
        student_gpa,
        student_major.title(),
        student_state.upper(),
        student_first_gen,
        student_financial_need
    )

    st.subheader(f"Scholarship matches for {student_name}")

    if matches.empty:
        st.warning("No matching scholarships found. Try changing your major or state.")
    else:
        for row_index, row in matches.iterrows():
            with st.container(border=True):
                st.markdown(f"### {row['name']}")
                st.write(f"**Match Score:** {row['match_score']}%")
                st.write(f"**Amount:** {row['amount']}")
                st.write(f"**Deadline:** {row['deadline']}")
                st.write(f"**Minimum GPA:** {row['min_gpa']}")
                st.write(f"**Major:** {row['major']}")
                st.write(f"**State:** {row['state']}")
                st.write(row["description"])
                st.link_button("Apply Here", row["link"])
else:
    st.info("Enter your profile in the sidebar to begin.")