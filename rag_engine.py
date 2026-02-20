import requests
from config import ROLE_ACCESS, OPENROUTER_API_KEY, OPENROUTER_MODEL, SYSTEM_PROMPT

def get_allowed_docs(documents, user_role):
    allowed_departments = ROLE_ACCESS.get(user_role, [])
    return [doc for doc in documents if doc["department"] in allowed_departments]

def call_openrouter(prompt):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8501",
            "X-Title": "Academic RAG Chatbot"
        },
        json={
            "model": OPENROUTER_MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        }
    )

    result = response.json()

    if response.status_code == 200 and "choices" in result:
        return result["choices"][0]["message"]["content"]
    else:
        return f"API Error: {result}"

def answer_question(query, user_role, vector_store):
    relevant_docs = vector_store.search(query)
    allowed_docs = get_allowed_docs(relevant_docs, user_role)

    context = "\n\n".join([doc["content"] for doc in allowed_docs])

    final_prompt = f"""
Context:
{context}

Question:
{query}
"""

    return call_openrouter(final_prompt)