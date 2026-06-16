import requests

def scrape_job_details(url: str) -> str:
    """
    Scrapes the text details from a job listing URL.
    Returns the raw/first part of the HTML text as a placeholder.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            # Simple fallback text extraction by removing tags
            import re
            html = response.text
            # Remove scripts and styles
            html = re.sub(r'<script.*?>.*?</script>', '', html, flags=re.DOTALL)
            html = re.sub(r'<style.*?>.*?</style>', '', html, flags=re.DOTALL)
            # Remove HTML tags
            text = re.sub(r'<.*?>', ' ', html)
            # Clean up whitespace
            cleaned_text = ' '.join(text.split())
            return cleaned_text[:3000]
    except Exception as e:
        return f"Could not scrape job details: {str(e)}"
    return "No details found."
