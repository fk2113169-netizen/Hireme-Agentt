import streamlit as st
from src.ui.components import inject_custom_css

def results_page():
    # Inject styling
    inject_custom_css()
    
    # Back to upload button
    if st.button("⬅️ Upload New CV"):
        st.session_state.stage = "upload"
        st.session_state.results = []
        st.session_state.cv_data = None
        st.rerun()
        
    st.markdown('<div class="main-title">💼 Recommendation Results</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI matched opportunities curated by HireMe Agent</div>', unsafe_allow_html=True)
    
    cv_data = st.session_state.cv_data
    results = st.session_state.results
    
    # Display CV Details Card
    if cv_data:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader(f"👤 Profile: {cv_data.get('name', 'Candidate')}")
        if cv_data.get('email'):
            st.markdown(f"📧 **Email:** {cv_data.get('email')}")
            
        st.write("---")
        st.markdown(f"**Professional Summary:**  \n*{cv_data.get('summary', 'No summary available.')}*")
        
        st.write("---")
        st.markdown("**Skills:**")
        skills_html = ""
        for skill in cv_data.get('skills', []):
            skills_html += f'<span class="badge badge-purple">{skill}</span>'
        st.markdown(skills_html or "*No skills parsed*", unsafe_allow_html=True)
        
        st.write("---")
        st.markdown("**Suggested Target Roles:**")
        roles_html = ""
        for role in cv_data.get('target_roles', []):
            roles_html += f'<span class="badge badge-blue">{role}</span>'
        st.markdown(roles_html or "*No target roles identified*", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Display Recommendations
    st.markdown("### 🔍 Evaluated Job Openings")
    if not results:
        st.info("No matching jobs found. Try adjusting target location or key criteria in your CV.")
    else:
        for job in results:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            col_details, col_score = st.columns([4, 1])
            
            with col_details:
                st.markdown(f"#### [{job['title']}]({job['url']})")
                st.write(f"🏢 **{job['company']}** — 📍 *{job['location']}*")
                
                # Show salary if present
                sal_min = job.get('salary_min')
                sal_max = job.get('salary_max')
                if sal_min and sal_max:
                    st.write(f"💰 **Salary range:** £{int(sal_min):,} - £{int(sal_max):,}")
                elif sal_min:
                    st.write(f"💰 **Salary:** £{int(sal_min):,}+")
                    
            with col_score:
                score = job.get('match_score', 50)
                st.markdown(f'<div class="score-circle">{score}%</div>', unsafe_allow_html=True)
                st.markdown('<div style="text-align: right; color:#3B82F6; font-weight:600; font-size:0.9rem;">Match</div>', unsafe_allow_html=True)
                
            st.write("---")
            st.markdown(f"**🤖 AI Match Explanation:**  \n{job.get('reasoning', '')}")
            st.write("---")
            st.markdown(f"**Job Description Snippet:**  \n*{job['description']}*")
            
            # Application Link
            st.markdown(
                f'<a href="{job["url"]}" target="_blank" style="text-decoration:none;"><button style="background-color: #2563EB !important; color: white; border: 1px solid #3B82F6; border-radius: 6px; font-weight: 600; padding: 10px 24px; width: 100%; box-shadow: 0 2px 10px rgba(37, 99, 235, 0.2); cursor: pointer; transition: all 0.2s ease; margin-top: 15px;">Apply to Job Post 🚀</button></a>',
                unsafe_allow_html=True
            )
            st.markdown('</div>', unsafe_allow_html=True)
