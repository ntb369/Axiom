import streamlit as st


def show():

    st.title("📁 Projects")

    st.write(
        "Manage your robotics project ideas and notes."
    )

    if "project_notes" not in st.session_state:
        st.session_state.project_notes = ""

    project_name = st.text_input(
        "Project Name",
        placeholder="Example: Autonomous Robot"
    )

    notes = st.text_area(
        "Project Notes",
        value=st.session_state.project_notes,
        height=300,
        placeholder="Write your project ideas, requirements, sensors, algorithms..."
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("💾 Save Notes"):

            st.session_state.project_notes = notes
            st.success("Project notes saved!")

    with col2:

        if st.button("🗑 Clear Notes"):

            st.session_state.project_notes = ""
            st.rerun()

    st.divider()

    st.subheader("Current Project")

    if project_name:
        st.write(f"**Project:** {project_name}")

    if st.session_state.project_notes:
        st.markdown(st.session_state.project_notes)