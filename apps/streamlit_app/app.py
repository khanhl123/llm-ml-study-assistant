import requests
import streamlit as st


API_BASE_URL = "http://localhost:8000"


st.set_page_config(page_title="LLM ML Study Assistant", page_icon="🤖")
st.title("LLM ML Study Assistant")
st.write(
    "Week 1 starter app: ask a question and receive a placeholder response from the FastAPI backend."
)

question = st.text_input("Enter your study question:")
submit_clicked = st.button("Submit")

if submit_clicked:
    if not question.strip():
        st.warning("Please enter a question before submitting.")
    else:
        try:
            response = requests.post(
                f"{API_BASE_URL}/query",
                json={"question": question},
                timeout=10,
            )
            response.raise_for_status()
            data = response.json()

            st.subheader("Answer")
            st.write(data.get("answer", "No answer returned."))

            st.subheader("Citations")
            citations = data.get("citations", [])
            if citations:
                for citation in citations:
                    st.write(f"- {citation}")
            else:
                st.write("No citations available.")
        except requests.exceptions.RequestException:
            st.error(
                "Could not connect to the backend. Make sure FastAPI is running at "
                "http://localhost:8000."
            )

