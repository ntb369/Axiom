import streamlit as st


def show():

    st.title("⚙️ Settings")

    st.write("Configure Axiom")

    st.divider()

    st.subheader("AI Model")

    st.selectbox(
        "Current Model",
        [
            "Llama 3.3 70B"
        ],
        disabled=True
    )

    st.divider()

    st.subheader("Chat")

    if st.button("🗑 Clear All Chat History"):

        keys = [
            "messages",
            "ros_messages",
            "code_messages",
            "hardware_messages"
        ]

        for key in keys:
            if key in st.session_state:
                del st.session_state[key]

        st.success("Chat history cleared!")

    st.divider()

    st.subheader("About Axiom")

    st.info(
        """
Axiom v1.0

AI Robotics Assistant

Powered by Groq + Llama 3.3

Designed to help students, engineers,
and robotics enthusiasts learn faster.
"""
    )

    st.divider()

    st.success("Version 1.0")