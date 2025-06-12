import streamlit as st
from main import ask_question  # make sure 'ask_question' filters LLM output

st.set_page_config(page_title="Car Info Chatbot", layout="centered")

st.markdown("<h1 style='text-align: center;'>🚗 Car Info Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask anything about classic cars from the dataset!</p>", unsafe_allow_html=True)

# Use session state to trigger when Enter is pressed
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def submit():
    st.session_state.submitted = True

user_input = st.text_input("Ask a question about a car:", key="user_input", on_change=submit)

if st.session_state.get("submitted"):
    with st.spinner("🤖 Thinking..."):
        try:
            answer = ask_question(st.session_state.user_input)
            st.markdown(f"**Answer:** {answer}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
    st.session_state.submitted = False  # reset after answer
