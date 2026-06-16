import json
import re
from google import genai
from google.genai import types
from src.config.settings import GEMINI_API_KEY

def search_jobs(query: str, location: str = "", results_per_page: int = 5, page: int = 1) -> list:
    """
    Searches for jobs on LinkedIn and Indeed using Gemini Google Search grounding.
    
    Args:
        query (str): Job title or keywords.
        location (str): Geographical location.
        results_per_page (int): Maximum number of results to retrieve.
        page (int): Page index (unused in search grounding, default: 1).
        
    Returns:
        list: Standardized list of jobs containing title, company, description, location, and URL.
    """
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not configured.")
        
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    prompt = f"""
    Search the web using Google Search to find {results_per_page} open job postings for '{query}' in '{location or "Worldwide"}'.
    Look specifically for direct job listings on Indeed (indeed.com) and LinkedIn (linkedin.com/jobs).
    
    For each job found, extract:
    - title (the job title)
    - company (the company offering the job)
    - location (the location of the job)
    - description (a 2-3 sentence snippet of the job requirements)
    - url (the direct job listing URL on LinkedIn or Indeed, not a Google search redirect)
    
    Return the results ONLY as a valid JSON list matching this format:
    [
      {{
        "title": "Job Title",
        "company": "Company Name",
        "location": "Location",
        "description": "Snippet of description",
        "url": "https://www.linkedin.com/jobs/view/..."
      }}
    ]
    No markdown formatting (like ```json), no other text. Return ONLY the JSON array.
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=[{'google_search': {}}],
                temperature=0.1
            )
        )
        
        # Clean response text to extract JSON array
        text = response.text.strip()
        if text.startswith("```"):
            text = re.sub(r'^```[a-zA-Z]*\n', '', text)
            text = re.sub(r'\n```$', '', text)
            text = text.strip()
            
        jobs = json.loads(text)
        
        formatted_jobs = []
        for job in jobs:
            formatted_jobs.append({
                'id': job.get('url'),
                'title': job.get('title'),
                'company': job.get('company', 'Unknown'),
                'description': job.get('description', ''),
                'location': job.get('location', location or 'Unknown'),
                'salary_min': None,
                'salary_max': None,
                'url': job.get('url')
            })
        return formatted_jobs
    except Exception as e:
        print(f"Gemini job search failed: {e}. Returning empty list.")
        return []
