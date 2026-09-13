import os
import logging

from dotenv import load_dotenv
from groq import Groq


# Load environment variables from .env
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)


if not GROQ_API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY is missing. "
        "Add it to your .env file."
    )


# Groq client
client = Groq(
    api_key=GROQ_API_KEY,
    timeout=60.0,
    max_retries=2
)


def get_ai_response(messages):
    """
    Send a conversation to Groq and return the response.
    """

    if not isinstance(messages, list):
        raise TypeError("messages must be a list.")

    if not messages:
        raise ValueError("Messages cannot be empty.")

    for message in messages:
        if not isinstance(message, dict):
            raise ValueError("Each message must be a dictionary.")

        if "role" not in message or "content" not in message:
            raise ValueError(
                "Each message must contain 'role' and 'content'."
            )

        if message["role"] not in [
            "system",
            "user",
            "assistant"
        ]:
            raise ValueError(
                f"Invalid message role: {message['role']}"
            )

        if not isinstance(message["content"], str):
            raise ValueError(
                "Message content must be a string."
            )

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.7,
            max_tokens=2048,
        )

        if not response.choices:
            raise RuntimeError(
                "Groq returned no response choices."
            )

        answer = response.choices[0].message.content

        if not answer:
            raise RuntimeError(
                "Groq returned an empty response."
            )

        return answer.strip()

    except Exception as error:
        logger.exception("Groq API request failed")

        # Show the actual error in the Streamlit interface
        import streamlit as st

        st.error(
            f"Groq API Error: {type(error).__name__}: {error}"
        )

        return (
            "I could not connect to the Groq AI service. "
            "Please check your API key, model name, and internet connection."
        )


def get_model_display_name():
    """
    Return the configured model name.
    """

    return MODEL_NAME