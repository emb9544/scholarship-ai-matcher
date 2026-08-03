import streamlit as st
from matcher import find_matches


st.set_page_config(
    page_title="Scholarship AI Matcher",
    page_icon="🎓",
    layout="wide",
)


st.title("🎓 Scholarship AI Matcher")
st.write(
    "Find scholarships that match your academic profile, "
    "background, and financial needs."
)


with st.sidebar:
    st.header("Student Profile")

    student_name = st.text_input(
        "Name",
        placeholder="Enter your name",
    )

    student_gpa = st.number_input(
        "GPA",
        min_value=0.0,
        max_value=4.0,
        step=0.1,
    )

    student_major = st.text_input(
        "Major",
        placeholder="Example: Computer Science",
    )

    student_state = st.text_input(
        "State of residence",
        placeholder="Example: NY",
    )

    student_first_gen = st.selectbox(
        "First-generation college student?",
        ["Yes", "No"],
    )

    student_financial_need = st.selectbox(
        "Financial need?",
        ["Yes", "No"],
    )

    student_interests = st.text_area(
        "Tell us about your interests, career goals, or background",
        placeholder=(
            "Example: I want to study software engineering "
            "and help underserved communities."
        ),
    )

    search_button = st.button(
        "Find Scholarships",
        use_container_width=True,
    )


if search_button:
    missing_fields = []

    if not student_name.strip():
        missing_fields.append("name")

    if not student_major.strip():
        missing_fields.append("major")

    if not student_state.strip():
        missing_fields.append("state")

    if missing_fields:
        missing_fields_text = ", ".join(missing_fields)

        st.error(
            f"Please complete the following fields: "
            f"{missing_fields_text}."
        )

    else:
        matches = find_matches(
            student_gpa,
            student_major.strip().title(),
            student_state.strip().upper(),
            student_first_gen,
            student_financial_need,
        )

        st.subheader(
            f"Scholarship matches for {student_name.strip()}"
        )

        if matches.empty:
            st.warning(
                "No matching scholarships were found. "
                "Try changing your major, state, or profile information."
            )

        else:
            st.success(
                f"We found {len(matches)} scholarship matches."
            )

            for row_index, scholarship in matches.iterrows():
                with st.container(border=True):
                    title_column, score_column = st.columns([3, 1])

                    with title_column:
                        st.markdown(
                            f"### {scholarship['name']}"
                        )

                    with score_column:
                        st.metric(
                            "Match Score",
                            f"{scholarship['match_score']}%",
                        )

                    amount_column, deadline_column = st.columns(2)

                    with amount_column:
                        st.write(
                            f"**Amount:** {scholarship['amount']}"
                        )

                    with deadline_column:
                        st.write(
                            f"**Deadline:** "
                            f"{scholarship['deadline']}"
                        )

                    st.write(
                        f"**Minimum GPA:** "
                        f"{scholarship['min_gpa']}"
                    )

                    st.write(
                        f"**Eligible majors:** "
                        f"{scholarship['major']}"
                    )

                    st.write(
                        f"**Eligible states:** "
                        f"{scholarship['state']}"
                    )

                    st.write(scholarship["description"])

                    scholarship_link = scholarship["link"]

                    if scholarship_link:
                        st.link_button(
                            "Apply Here",
                            scholarship_link,
                        )

else:
    st.info(
        "Enter your profile in the sidebar and click "
        "'Find Scholarships' to begin."
    )