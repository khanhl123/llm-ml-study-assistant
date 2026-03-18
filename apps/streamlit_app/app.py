import requests
import streamlit as st

API_BASE_URL = "http://localhost:8000"

st.set_page_config(page_title="LLM ML Study Assistant", page_icon="📚")

st.title("LLM ML Study Assistant")
st.caption(
    "A cited ML study assistant — ask a question and receive a grounded answer with sources. "
    "(Week 1: placeholder responses)"
)

st.divider()

question = st.text_input("Your question", placeholder="e.g. What is the bias-variance tradeoff?")
submit_clicked = st.button("Submit", type="primary")

if submit_clicked:
    if not question.strip():
        st.warning("Please enter a question before submitting.")
    else:
        with st.spinner("Fetching answer..."):
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
                        st.markdown(f"- {citation}")
                else:
                    st.write("No citations available.")

            except requests.exceptions.ConnectionError:
                st.error(
                    "Could not connect to the backend. "
                    "Make sure FastAPI is running at http://localhost:8000."
                )
            except requests.exceptions.HTTPError as e:
                st.error(f"Backend returned an error: {e}")
            except requests.exceptions.RequestException as e:
                st.error(f"Unexpected error: {e}")