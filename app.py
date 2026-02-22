# app.py
import streamlit as st
from search import retrieve
from summarize_chunks import summarize_chunks
from final_answer import answer_from_summaries

st.set_page_config(page_title="Medical RAG Assistant", layout="wide")
st.title("🩺 Medical RAG Assistant")
st.write("Ask questions based on your uploaded medical PDF (CPR Guidelines).")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
query = st.chat_input("Ask a question...")

if query:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            # --- Initialize variables ---
            docs = []
            summaries = []
            answer = None

            # --- 1️⃣ Casual / small talk responses ---
            casual_responses = {
                "hello": "Hi there! How can I help you today?",
                "hi": "Hello! How can I assist you?",
                "hey": "Hey! Ask me anything about CPR or first aid.",
                "how are you": "I'm a bot, but thanks for asking! Ask me about CPR or first aid.",
                "thanks": "You're welcome! Do you have more questions about CPR?",
                "thank you": "You're welcome! Do you have more questions about CPR?",
            }

            normalized = query.lower().strip()
            for key in casual_responses:
                if key in normalized:
                    answer = casual_responses[key]
                    break

            # --- 2️⃣ Medical RAG flow ---
            if not answer:
                # Retrieve relevant chunks from PDF
                docs = retrieve(query)

                if docs:  # if any relevant chunks found
                    top_docs = docs[:3]  # top 3 chunks
                    summaries = summarize_chunks(top_docs)  # ultra-concise summaries
                    answer = answer_from_summaries(summaries, query)
                else:
                    # No relevant info found
                    answer = "I don't have information on that. Please ask a CPR or first aid related question."

            # Display the final answer
            st.markdown(answer)

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": answer})