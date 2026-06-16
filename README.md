# HireMe Agent

A Python-based agentic job application assistant using Gemini AI and Google Search grounding to match resumes against live jobs on LinkedIn and Indeed.

🔗 **Live Demo**: [https://fk2113169-netizen-hireme-agent-app-wyjd0q.streamlit.app/](https://fk2113169-netizen-hireme-agent-app-wyjd0q.streamlit.app/)

## Features
- **CV Parsing**: Automatically extracts text from PDF/DOCX resumes and parses structured details (skills, roles, summaries) using `gemini-2.5-flash`.
- **Indeed & LinkedIn Search**: Queries live listings using Google Search grounding.
- **Match Scoring**: Evaluates candidate suitability and generates matching scores (0-100%) with custom reasoning.
- **Sleek Interface**: Clean, professional dark mode UI.

## Setup Instructions

### 1. Install Requirements
Create a virtual environment (optional but recommended) and install the dependencies:
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create a `.env` file in the root of the project and fill in your keys:
```env
GEMINI_API_KEY=your_gemini_api_key_here
ADZUNA_APP_KEY=your_adzuna_app_key_here
ADZUNA_APP_ID=your_adzuna_app_id_here
ADZUNA_COUNTRY=gb
```

### 3. Run the Application
Start the Streamlit application using:
```bash
streamlit run app.py
```
