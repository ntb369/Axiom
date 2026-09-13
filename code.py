import streamlit as st
from ai_service import get_ai_response


def show():

    st.title("💻 Code Generator")

    st.markdown("""
Generate code for:

- Python
- C++
- Arduino
- ESP32
- ROS
- OpenCV
- Machine Learning
- Robotics Projects
""")

    if "code_messages" not in st.session_state:
        st.session_state.code_messages = []

    # Show previous chat
    for message in st.session_state.code_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Describe the code you need...")

    if prompt:

        st.session_state.code_messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        conversation = [
            {
                "role": "system",
                "content": """
You are Axiom.

You are an expert Robotics Software Engineer.

Generate professional, complete, runnable code.

You specialize in:

- Python
- C++
- Arduino
- ESP32
- ROS & ROS2
- OpenCV
- AI
- Machine Learning
- Robotics Algorithms

Rules:

1. Always generate complete code.
2. Explain the code after generating it.
3. Use best coding practices.
4. Never return incomplete code.
5. Format code properly using markdown.
"""
            }
        ]

        conversation.extend(st.session_state.code_messages)

        try:

            with st.chat_message("assistant"):

                with st.spinner("Generating code..."):

                    answer = get_ai_response(conversation)

                    st.markdown(answer)

            st.session_state.code_messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        except Exception as e:
            st.error(e)