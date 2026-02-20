ROLE_ACCESS = {
    "Admission_Officer": ["Admissions"],
    "Faculty": ["Academics"],
    "Hostel_Admin": ["Hostel"],
    "Placement_Officer": ["Placements"],
    "Admin": ["Admissions", "Academics", "Hostel", "Placements"]
}

DATA_FOLDER = "enterprise_data"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

LLM_PROVIDER = "openrouter"

OPENROUTER_API_KEY = "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"
OPENROUTER_MODEL = "mistralai/mistral-7b-instruct"

SYSTEM_PROMPT = '''
You are an official AI assistant for ABC Engineering College.

Provide accurate information about Admissions, Academics,
Hostel, and Placements.

Only answer from provided context.
If information is missing say:
"This information is not available in the college database."
'''