import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")

st.title("Groq Chatbot")
st.caption("ask anything below")
st.divider()

# ...........chat.....form.........
with st.form("chat_form"):
    user_input=st.text_area("your message",placeholder="type your question here")
    submitted=st.form_submit_button("send")

if submitted:
    llm=ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0,
        max_tokens=None,
        reasoning_format="parsed",
        timeout=None,
        max_retries=2,
        api_key=api_key



    )
    with st.spinner("Thinking....."):
          response=llm.invoke([
        SystemMessage(content="you are helpful assistant"),
        HumanMessage(content=user_input)
  
    ])

    st.divider()
    st.subheader("Answer")
    st.write(response.content)

