from src.tools.job_search import search_jobs
from src.tools.job_scraper import scrape_job_details

# Map tool names to functions
TOOL_REGISTRY = {
    "search_jobs": search_jobs,
    "scrape_job_details": scrape_job_details
}

def get_tool(name: str):
    """Retrieves a tool function by name."""
    return TOOL_REGISTRY.get(name)
