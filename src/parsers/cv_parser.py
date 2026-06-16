import json
from google import genai
from google.genai import types
from src.config.settings import GEMINI_API_KEY

def parse_cv_with_gemini(cv_text: str) -> dict:
    """Parses CV text into a structured dictionary using Gemini API."""
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not configured.")
        
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    prompt = f"""
    You are an expert CV and resume parsing agent.
    Analyze the resume text below and extract structured information.
    Provide the response in the following JSON format:
    {{
      "name": "Candidate Name (or None if not found)",
      "email": "Candidate Email (or None if not found)",
      "skills": ["Skill 1", "Skill 2", ...],
      "experience": ["Job title 1 - Company 1 - Years", "Job title 2 - Company 2 - Years"],
      "target_roles": ["Suggested/Target Job Role 1", "Suggested/Target Job Role 2"],
      "summary": "Short 2-3 sentence professional summary"
    }}
    
    Resume Text:
    {cv_text}
    """

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.1,
        ),
    )
    
    try:
        # Load output
        parsed_data = json.loads(response.text)
        return parsed_data
    except Exception as e:
        # Fallback parsing in case of error
        return {
            "name": "Unknown",
            "email": "Unknown",
            "skills": [],
            "experience": [],
            "target_roles": ["Software Engineer"],
            "summary": "Error parsing resume: " + str(e)
        }
