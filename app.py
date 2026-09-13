import streamlit as st

import chat
print("Chat module loaded from:", chat.__file__)

import ros
import code
import hardware
import documents
import projects
import settings

# -----------------------------
# DEBUG (Temporary)
# -----------------------------
print("Chat module loaded from:", chat.__file__)

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Axiom",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🤖 Axiom")
    st.caption("Beyond the Prompt.")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "💬 Chat",
            "🤖 ROS Assistant",
            "💻 Code Generator",
            "🔧 Hardware Advisor",
            "📄 Documents",
            "📁 Projects",
            "⚙️ Settings"
        ]
    )

    st.divider()

    if st.button("🗑 Clear Chat"):

        keys = [
            "messages",
            "ros_messages",
            "code_messages",
            "hardware_messages"
        ]

        for key in keys:
            if key in st.session_state:
                del st.session_state[key]

        st.rerun()

# -----------------------------
# Navigation
# -----------------------------
if page == "💬 Chat":

    chat.show()

elif page == "🤖 ROS Assistant":

    ros.show()

elif page == "💻 Code Generator":

    code.show()

elif page == "🔧 Hardware Advisor":

    hardware.show()

elif page == "📄 Documents":

    documents.show()

elif page == "📁 Projects":

    projects.show()

elif page == "⚙️ Settings":

    settings.show()