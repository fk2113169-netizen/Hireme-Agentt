import os
import json
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)

prompt = """
Search the web using Google Search to find 3 open jobs for 'Python Developer' in 'London' posted on LinkedIn or Indeed.
For each job found, extract:
- Title
- Company
- Location
- Job page URL (this must be the direct LinkedIn or Indeed job listing URL, not a google search URL)
- Brief description

Return the results ONLY as a valid JSON list of objects matching this schema:
[
  {
    "title": "Job Title",
    "company": "Company Name",
    "location": "Location",
    "description": "Brief description",
    "url": "https://www.linkedin.com/jobs/view/..."
  }
]
No markdown surrounding the JSON, no backticks, no other text. Just the JSON.
"""

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        tools=[{'google_search': {}}],
        temperature=0.1
    )
)
print("Response text:")
print(response.text)
