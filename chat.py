import streamlit as st
from memory import remember, get_memory_prompt
from ai_service import get_ai_response
from knowledge import search_knowledge

st.write("WELCOME TO AXIOM 🤖")
def show():

    st.title("🤖 Axiom")
    st.subheader("AI Robotics Assistant")

    st.write(
        "Ask anything about Robotics, ROS, Arduino, ESP32, Python, C++, or AI."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask Axiom anything...")

    if prompt:

        remember(prompt)

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("Axiom is thinking..."):

                # ---------- KNOWLEDGE BASE ----------
                answer = search_knowledge(prompt)

                # ---------- AI ----------
                if answer is None:

                    conversation = []

                    memory_prompt = get_memory_prompt()

                    if memory_prompt:
                        conversation.append(
                            {
                                "role": "system",
                                "content": memory_prompt
                            }
                        )

                    conversation.extend(st.session_state.messages)

                    answer = get_ai_response(conversation)

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )