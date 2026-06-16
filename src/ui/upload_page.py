import streamlit as st
from src.ui.components import inject_custom_css
from src.parsers.cv_extractor import extract_cv_text
from src.parsers.cv_parser import parse_cv_with_gemini
from src.memory.cv_store import save_cv
from src.agents.hire_agent import run_job_search_agent

def upload_page():
    # Inject premium styles
    inject_custom_css()
    
    # UI Header
    st.markdown('<div class="main-title">💼 HireMe Agent</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-Powered Job Recommendation & Matching Engine</div>', unsafe_allow_html=True)
    
    # Glassmorphism container for inputs
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    st.subheader("Upload Your CV / Resume")
    uploaded_file = st.file_uploader(
        "Supported formats: PDF, DOCX (Max 200MB)",
        type=["pdf", "docx"],
        label_visibility="collapsed"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        location_input = st.text_input(
            "Target Location (e.g., London, Remote)",
            value=st.session_state.location,
            placeholder="City, Country or Remote"
        )
    with col2:
        count_input = st.slider(
            "Max Job Matches",
            min_value=1,
            max_value=10,
            value=st.session_state.count
        )
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Error display if any occurred in previous attempts
    if st.session_state.error:
        st.error(f"⚠️ {st.session_state.error}")
        # Reset error after displaying
        st.session_state.error = None
        
    # Submit button
    if st.button("Analyze CV & Find Matching Jobs"):
        if not uploaded_file:
            st.warning("Please upload a PDF or DOCX resume to continue.")
            return
            
        with st.spinner("✨ Step 1: Extracting text from resume..."):
            try:
                file_bytes = uploaded_file.read()
                file_name = uploaded_file.name
                
                # Extract plain text
                cv_text = extract_cv_text(file_name, file_bytes)
                
            except Exception as e:
                st.session_state.error = f"Failed to extract text from file: {str(e)}"
                st.rerun()
                return

        with st.spinner("🧠 Step 2: Parsing CV details using Gemini AI..."):
            try:
                # Parse with Gemini
                cv_data = parse_cv_with_gemini(cv_text)
                
                # Save to in-memory store
                save_cv(cv_data)
                st.session_state.cv_data = cv_data
                
            except Exception as e:
                st.session_state.error = f"Gemini Parsing Error: {str(e)}"
                st.rerun()
                return

        with st.spinner("🔍 Step 3: Searching & evaluating matched jobs..."):
            try:
                # Fetch location and count values
                st.session_state.location = location_input
                st.session_state.count = count_input
                
                # Run Agent Matching
                results = run_job_search_agent(
                    cv_data=cv_data,
                    location=location_input,
                    count=count_input
                )
                
                st.session_state.results = results
                st.session_state.stage = "results"
                st.rerun()
                
            except Exception as e:
                st.session_state.error = f"Job Agent Error: {str(e)}"
                st.rerun()
                return
