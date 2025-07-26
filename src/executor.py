import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def choose_model():
    preferred_models = [
        "models/gemini-2.5-pro",
        "models/gemini-1.5-flash-latest",
        "models/gemini-1.5-pro"
    ]
    models = list(genai.list_models())
    for preferred in preferred_models:
        if any(m.name == preferred for m in models):
            return preferred
    for m in models:
        if "generateContent" in getattr(m, "supported_generation_methods", []):
            return m.name
    raise Exception("No model with 'generateContent' capability found.")

def generate_response(prompt):
    model_name = choose_model()
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    return response.text.strip()
