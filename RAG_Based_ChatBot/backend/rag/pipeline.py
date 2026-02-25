""" 
CURRENT STRCUTURE :
        PDF → Embeddings → Chroma

        User Question
        ↓
        Retriever
        ↓
        Generator
        ↓
        Answer
       
After adding pipeline: 
        User Question
        ↓
        rag_pipeline()
        ↓
        Retriever
        ↓
        Generator
        ↓
        Answer
        
Why This Is Important (Professional Reason)

When you build FastAPI, your endpoint should not know about:

        Chroma
        Azure
        Embeddings
        Context injection
        Prompt engineering

It should just do:

@app.post("/chat")
def chat(request):
    return rag_pipeline(request.message)

That’s clean separation of concerns.
"""

from .retriever import retrieve_context
from .generator import generate_answer


def rag_pipeline(question: str, top_k: int = 3):

    # Step 1: Retrieve relevant chunks
    documents = retrieve_context(question, top_k=top_k)
    context = "\n\n".join(documents)

    # Step 2: Generate final answer
    answer = generate_answer(question, context)

    return answer


if __name__ == "__main__":
    while True:
        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        response = rag_pipeline(question)
        print("\n🤖 Answer:\n")
        print(response)