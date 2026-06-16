import streamlit as st

def inject_custom_css():
    """Injects a minimalist, professional design using only black, blue, and white styling."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

        /* Clean black/dark slate background */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            font-family: 'Outfit', sans-serif;
            background-color: #060913 !important; /* Professional dark blue-black */
            background-image: none !important;
            color: #FFFFFF !important;
        }
        
        /* Sidebar styling override */
        [data-testid="stSidebar"] {
            background-color: #0A0F1D !important;
            border-right: 1px solid #1E293B;
        }

        /* Title styling - Clean Solid White */
        .main-title {
            color: #FFFFFF !important;
            font-size: 2.6rem;
            font-weight: 700;
            text-align: center;
            margin-bottom: 0.2rem;
            letter-spacing: -0.5px;
        }

        /* Subtitle - Professional Blue */
        .subtitle {
            text-align: center;
            color: #3B82F6;
            font-size: 1.05rem;
            margin-bottom: 2rem;
            font-weight: 400;
            letter-spacing: 0.5px;
        }

        /* Solid Dark Card Containers with Subtle Blue/Grey Borders */
        .glass-card {
            background: #0A0F1D;
            border: 1px solid #1E293B;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        }

        /* Job Cards with hover interaction */
        .job-card {
            background: #0D1527;
            border: 1px solid #1E293B;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 18px;
            transition: all 0.25s ease;
        }
        .job-card:hover {
            transform: translateY(-2px);
            border-color: #3B82F6;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.15);
        }

        /* Badges - clean blue, black, and white borders */
        .badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
            margin-right: 6px;
            margin-bottom: 6px;
            color: #FFFFFF !important;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .badge-purple {
            background: #1E3A8A; /* Navy Blue */
            border: 1px solid #3B82F6;
        }
        .badge-blue {
            background: #0F172A; /* Slate */
            border: 1px solid #475569;
        }
        .badge-green {
            background: #0B1F19; /* Deep Slate Green */
            border: 1px solid #10B981;
        }

        /* Match Score circles (Professional Blue) */
        .score-circle {
            font-size: 2.2rem;
            font-weight: 700;
            color: #3B82F6 !important;
            text-align: right;
        }
        
        /* Modern form inputs & button styling - clean blue & white */
        .stButton>button {
            background-color: #2563EB !important;
            background-image: none !important;
            color: #FFFFFF !important;
            border: 1px solid #3B82F6 !important;
            border-radius: 6px !important;
            font-weight: 600 !important;
            padding: 8px 20px !important;
            box-shadow: 0 2px 10px rgba(37, 99, 235, 0.2) !important;
            transition: all 0.2s ease !important;
        }
        .stButton>button:hover {
            background-color: #1D4ED8 !important;
            border-color: #2563EB !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3) !important;
        }

        /* Form Controls Styling */
        input, select, textarea {
            background-color: #0D1527 !important;
            border: 1px solid #1E293B !important;
            color: #FFFFFF !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
