import streamlit as st
from ai_service import get_ai_response


def show():

    st.title("🔧 Hardware Advisor")

    st.markdown("""
Need help selecting hardware?

Ask about:

- Arduino
- ESP32
- Raspberry Pi
- STM32
- NVIDIA Jetson
- Motors
- Motor Drivers
- Batteries
- LiDAR
- Cameras
- Sensors
- Power Supply
- Electronics
- PCB Design
""")

    if "hardware_messages" not in st.session_state:
        st.session_state.hardware_messages = []

    # Display previous messages
    for message in st.session_state.hardware_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask a hardware question...")

    if prompt:

        st.session_state.hardware_messages.append(
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

You are an expert Robotics Hardware Engineer.

Your expertise includes:

- Arduino
- ESP32
- Raspberry Pi
- STM32
- NVIDIA Jetson
- Sensors
- LiDAR
- Cameras
- IMU
- GPS
- Encoders
- Motors
- Servo Motors
- Stepper Motors
- BLDC Motors
- Motor Drivers
- Power Electronics
- PCB Design
- Embedded Systems

Rules:

1. Recommend the best hardware for the user's project.
2. Explain why you recommend it.
3. Compare alternatives when appropriate.
4. Suggest practical wiring and safety tips.
5. Keep explanations clear and beginner-friendly.
"""
            }
        ]

        conversation.extend(st.session_state.hardware_messages)

        try:

            with st.chat_message("assistant"):

                with st.spinner("Analyzing hardware..."):

                    answer = get_ai_response(conversation)

                    st.markdown(answer)

            st.session_state.hardware_messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        except Exception as e:
            st.error(e)