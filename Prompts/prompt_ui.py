from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

st.header("BlogQuestAI")

user_input = st.text_input("Enter your prompt")


if st.button('summarize'): 
    result = model.invoke(user_input)
    st.write(result.content)
