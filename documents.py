import streamlit as st
from ai_service import get_ai_response


def show():

    st.title("📄 Document Assistant")

    st.write(
        "Paste text from a PDF, research paper, documentation, or robotics manual below."
    )

    document = st.text_area(
        "Document Content",
        height=300,
        placeholder="Paste your document here..."
    )

    question = st.text_input(
        "Ask a question about the document"
    )

    if st.button("Analyze Document"):

        if document.strip() == "":
            st.warning("Please paste some document text.")
            return

        conversation = [
            {
                "role": "system",
                "content": """
You are Axiom.

You are an expert document analysis assistant.

You summarize documents,
answer questions,
explain technical concepts,
and simplify difficult content.

Always give structured answers.
"""
            },
            {
                "role": "user",
                "content": f"""
Document:

{document}

Question:

{question}
"""
            }
        ]

        try:

            with st.spinner("Analyzing document..."):

                answer = get_ai_response(conversation)

            st.subheader("Answer")

            st.markdown(answer)

        except Exception as e:
            st.error(e)