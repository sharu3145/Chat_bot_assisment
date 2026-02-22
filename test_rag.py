from search import retrieve
from generate import generate_answer

query = "What is CPR?"

# Step 1: Retrieve
docs = retrieve(query)

# Step 2: Combine context
context = "\n\n".join(docs)

# Step 3: Generate answer
answer = generate_answer(context, query)

print("\nANSWER:\n")
print(answer)