import json
from google import genai
from google.genai import types
from src.config.settings import GEMINI_API_KEY
from src.tools.job_search import search_jobs

def run_job_search_agent(cv_data: dict, location: str = "", count: int = 3) -> list:
    """
    Search agent that:
    1. Reads candidate's skills and target roles.
    2. Searches for jobs using the Adzuna API.
    3. Evaluates search results using Gemini to rate the match and explain why.
    """
    target_roles = cv_data.get("target_roles", ["Software Engineer"])
    skills = cv_data.get("skills", [])
    
    # Run searches for target roles
    all_jobs = []
    # Search for the first couple of target roles
    for role in target_roles[:2]:
        try:
            # We search for the role
            jobs = search_jobs(query=role, location=location, results_per_page=count)
            all_jobs.extend(jobs)
        except Exception as e:
            print(f"Error searching for {role}: {e}")
            
    # Deduplicate jobs by URL or ID
    seen = set()
    deduped_jobs = []
    for job in all_jobs:
        job_id = job.get('id') or job.get('url')
        if job_id not in seen:
            seen.add(job_id)
            deduped_jobs.append(job)
            
    # Limit to maximum count to avoid API overhead
    jobs_to_eval = deduped_jobs[:count]
    
    if not jobs_to_eval:
        return []
        
    # Evaluate each job using Gemini
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not configured.")
        
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    evaluated_jobs = []
    for job in jobs_to_eval:
        prompt = f"""
        You are an AI career advisor and matching assistant. Compare the candidate's CV profile against the job description below.
        
        Candidate Profile:
        - Target Roles: {', '.join(target_roles)}
        - Skills: {', '.join(skills)}
        - Experience: {json.dumps(cv_data.get('experience', []))}
        - Summary: {cv_data.get('summary', '')}
        
        Job Post:
        - Title: {job['title']}
        - Company: {job['company']}
        - Location: {job['location']}
        - Description: {job['description']}
        
        Rate the match out of 100 and provide a brief explanation (2-3 sentences max) highlighting:
        1. Key matches (why they fit).
        2. Gaps (what is missing).
        
        Respond ONLY in the following JSON format:
        {{
          "match_score": 85,
          "reasoning": "Candidate has strong Python and Streamlit experience matching the job description, but lacks the required Docker skills."
        }}
        """
        
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    temperature=0.1,
                ),
            )
            eval_data = json.loads(response.text)
            job['match_score'] = int(eval_data.get('match_score', 50))
            job['reasoning'] = eval_data.get('reasoning', 'No reasoning provided.')
        except Exception as e:
            job['match_score'] = 50
            job['reasoning'] = f"Failed to evaluate match: {str(e)}"
            
        evaluated_jobs.append(job)
        
    # Sort by match score descending
    evaluated_jobs.sort(key=lambda x: x.get('match_score', 0), reverse=True)
    return evaluated_jobs
