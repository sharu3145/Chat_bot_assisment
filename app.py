import streamlit as st
from search import retrieve
from generate import generate_answer

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
            
            # Step 1: Retrieve relevant chunks
            docs = retrieve(query)
            context = "\n\n".join(docs)

            # Step 2: Generate answer
            answer = generate_answer(context, query)

            st.markdown(answer)

            # Optional: Show retrieved context
            with st.expander("🔎 Retrieved Chunks"):
              for i, doc in enumerate(docs):
                st.markdown(f"**Chunk {i+1}:**")
                st.write(doc)
                st.markdown("---")

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": answer})