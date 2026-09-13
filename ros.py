import streamlit as st
from ai_service import get_ai_response


def show():

    st.title("🤖 ROS Assistant")

    st.markdown("""
Welcome to the **ROS Assistant**.

Ask anything about:

- ROS1
- ROS2
- Nodes
- Topics
- Publishers
- Subscribers
- Services
- Actions
- Gazebo
- RViz
- Navigation2
- MoveIt
- TF2
- URDF
- Xacro
- SLAM
""")

    if "ros_messages" not in st.session_state:
        st.session_state.ros_messages = []

    # Show chat history
    for message in st.session_state.ros_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask a ROS question...")

    if prompt:

        st.session_state.ros_messages.append(
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

You are a professional Robotics Engineer.

You ONLY answer questions related to:

- ROS
- ROS2
- Gazebo
- RViz
- MoveIt
- Navigation2
- TF2
- URDF
- Xacro
- Robot Localization
- SLAM

Explain concepts clearly.

If code is requested,
always provide complete runnable code.

Always answer like a robotics mentor.
"""
            }

        ]

        conversation.extend(st.session_state.ros_messages)

        try:

            with st.chat_message("assistant"):

                with st.spinner("Thinking..."):

                    answer = get_ai_response(conversation)

                    st.markdown(answer)

            st.session_state.ros_messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        except Exception as e:
            st.error(e)