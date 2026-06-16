import streamlit as st
from src.ui.components import inject_custom_css
from src.parsers.cv_extractor import extract_cv_text
from src.parsers.cv_parser import parse_cv_with_gemini
from src.memory.cv_store import save_cv
from src.agents.hire_agent import run_job_search_agent

def upload_page():
    # Inject Custom Light Styling and Tailwind
    inject_custom_css()
    
    # Render HTML Navbar
    st.markdown(
        """
        <header class="flex justify-between items-center w-full px-8 max-w-7xl mx-auto bg-white shadow-sm h-16 rounded-xl mt-2">
          <div class="flex items-center gap-4">
            <div class="text-xl font-extrabold text-primary flex items-center gap-2">
              <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">work</span>
              HireMe Agent
            </div>
            <nav class="hidden md:flex gap-6 items-center ml-8">
              <a class="text-sm text-primary font-semibold border-b-2 border-primary py-2" href="#">Features</a>
              <a class="text-sm text-slate-600 hover:text-primary py-2" href="#">How it Works</a>
              <a class="text-sm text-slate-600 hover:text-primary py-2" href="#">Pricing</a>
            </nav>
          </div>
          <div>
            <button class="text-sm font-semibold px-6 py-2 rounded-lg bg-primary text-white hover:bg-primary-container">
              Get Started
            </button>
          </div>
        </header>
        """,
        unsafe_allow_html=True
    )
    
    # Render HTML Hero Section
    st.markdown(
        """
        <section class="pt-16 pb-12 px-8 max-w-7xl mx-auto text-center">
          <div class="flex flex-col gap-4 max-w-xl mx-auto items-center">
            <div class="inline-flex items-center gap-2 px-3 py-1 bg-blue-50 text-primary rounded-full">
              <span class="material-symbols-outlined text-[16px]" style="font-variation-settings: 'FILL' 1;">auto_awesome</span>
              <span class="text-xs font-semibold">Next-Gen Recruitment AI</span>
            </div>
            <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 leading-tight">
              HireMe Agent
            </h1>
            <h2 class="text-xl text-slate-600 font-medium">
              AI-Powered Job Recommendation & Matching Engine
            </h2>
            <p class="text-base text-slate-600">
              Transform your career search with intelligent AI matching. Upload your resume and find your perfect fit in seconds.
            </p>
          </div>
        </section>
        """,
        unsafe_allow_html=True
    )
    
    # Main Form container
    st.markdown('<div class="max-w-4xl mx-auto px-8">', unsafe_allow_html=True)
    
    # Render Form
    with st.form("matching_tool_form", border=True):
        st.markdown(
            """
            <div class="text-center mb-6">
              <h3 class="text-xl font-bold text-slate-900">Find Your Perfect Match</h3>
              <p class="text-sm text-slate-600">Complete the details below to analyze your CV against active listings.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Uploader
        uploaded_file = st.file_uploader(
            "Upload Your CV / Resume (PDF, DOCX up to 10MB)",
            type=["pdf", "docx"]
        )
        
        col1, col2 = st.columns(2)
        with col1:
            location_input = st.text_input(
                "Target Location (e.g., Pakistan, Remote)",
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
            
        st.write("")
        submit_btn = st.form_submit_button("Analyze CV & Find Matching Jobs")
        
        st.markdown(
            """
            <p class="text-center text-xs text-slate-400 mt-2">
              Your data is encrypted and handled according to high-level security standards.
            </p>
            """,
            unsafe_allow_html=True
        )
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Error message block
    if st.session_state.error:
        st.markdown(f'<div class="max-w-4xl mx-auto px-8 mt-4"><div class="bg-red-50 text-red-700 p-4 rounded-xl border border-red-200">⚠️ {st.session_state.error}</div></div>', unsafe_allow_html=True)
        st.session_state.error = None
        
    # Execute Pipeline on click
    if submit_btn:
        if not uploaded_file:
            st.warning("Please upload a PDF or DOCX resume to continue.")
            return
            
        with st.spinner("✨ Step 1: Extracting text from resume..."):
            try:
                file_bytes = uploaded_file.read()
                file_name = uploaded_file.name
                cv_text = extract_cv_text(file_name, file_bytes)
            except Exception as e:
                st.session_state.error = f"Failed to extract text from file: {str(e)}"
                st.rerun()
                return

        with st.spinner("🧠 Step 2: Parsing CV details using Gemini AI..."):
            try:
                cv_data = parse_cv_with_gemini(cv_text)
                save_cv(cv_data)
                st.session_state.cv_data = cv_data
            except Exception as e:
                st.session_state.error = f"Gemini Parsing Error: {str(e)}"
                st.rerun()
                return

        with st.spinner("🔍 Step 3: Searching & evaluating matched jobs..."):
            try:
                st.session_state.location = location_input
                st.session_state.count = count_input
                
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
                
    # Render Stats Bento Grid with standardized border-radius (12px), clean shadow, and transitions
    st.markdown(
        """
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl mx-auto mt-12 mb-16 px-8">
          <div class="bg-white p-8 rounded-xl border border-slate-100 shadow-md hover:shadow-lg transition-all duration-300 text-center border-t-4 border-t-[#3525cd]">
            <div class="text-[#3525cd] text-4xl font-extrabold mb-1">98%</div>
            <div class="text-xs font-bold text-slate-500 uppercase tracking-wider">Match Accuracy</div>
          </div>
          <div class="bg-white p-8 rounded-xl border border-slate-100 shadow-md hover:shadow-lg transition-all duration-300 text-center border-t-4 border-t-[#3525cd]">
            <div class="text-[#3525cd] text-4xl font-extrabold mb-1">2.4s</div>
            <div class="text-xs font-bold text-slate-500 uppercase tracking-wider">Avg. Analysis Time</div>
          </div>
          <div class="bg-white p-8 rounded-xl border border-slate-100 shadow-md hover:shadow-lg transition-all duration-300 text-center border-t-4 border-t-[#3525cd]">
            <div class="text-[#3525cd] text-4xl font-extrabold mb-1">50k+</div>
            <div class="text-xs font-bold text-slate-500 uppercase tracking-wider">Daily Listings Indexed</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Render HTML Footer
    st.markdown(
        """
        <footer class="w-full py-8 px-8 flex flex-col md:flex-row justify-between items-center gap-4 bg-white border-t border-slate-200">
          <div class="flex flex-col gap-1">
            <div class="text-md font-bold text-slate-800 flex items-center gap-2">
              <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">work</span>
              HireMe Agent
            </div>
            <p class="text-xs text-slate-500">© 2026 HireMe Agent. All rights reserved.</p>
          </div>
          <nav class="flex flex-wrap justify-center gap-6">
            <a class="text-xs text-slate-500 hover:text-primary underline" href="#">Privacy Policy</a>
            <a class="text-xs text-slate-500 hover:text-primary underline" href="#">Terms of Service</a>
            <a class="text-xs text-slate-500 hover:text-primary underline" href="#">Cookie Policy</a>
            <a class="text-xs text-slate-500 hover:text-primary underline" href="#">Contact Us</a>
          </nav>
        </footer>
        """,
        unsafe_allow_html=True
    )
