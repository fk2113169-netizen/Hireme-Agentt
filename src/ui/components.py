import streamlit as st

def inject_custom_css():
    """Injects high-contrast, standardized, and professionally polished UI style definitions."""
    st.markdown(
        """
        <!-- Load Tailwind CSS and Web Fonts -->
        <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
        
        <script>
            tailwind.config = {
              theme: {
                extend: {
                  colors: {
                    primary: "#3525cd",
                    "primary-container": "#4f46e5",
                    "surface-white": "#FFFFFF",
                    "surface-soft": "#F1F5F9",
                    "background": "#f7f9fb",
                    "slate-900": "#0F172A",
                    "slate-600": "#475569",
                  }
                }
              }
            }
        </script>
        
        <style>
        /* Force high-contrast, clean light background */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            font-family: 'Inter', sans-serif !important;
            background-color: #f8fafc !important; 
            color: #0f172a !important;
        }

        /* Sidebar styling */
        [data-testid="stSidebar"], [data-testid="stSidebar"] * {
            background-color: #ffffff !important;
            border-right: 1px solid #e2e8f0;
            color: #0f172a !important;
        }

        /* Hide default headers & footers */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* Typography tightening & color contrast */
        h1, h2, h3, h4, h5, h6, 
        p, span, label, li, a, div, 
        .stText, [data-testid="stMarkdownContainer"] p, [data-testid="stWidgetLabel"] p {
            color: #0f172a !important; 
            font-family: 'Inter', sans-serif !important;
            letter-spacing: -0.01em !important;
        }
        
        .main-title {
            color: #0f172a !important;
            font-weight: 800 !important;
        }
        
        .subtitle {
            color: #2563eb !important;
            font-weight: 600 !important;
        }

        /* Design Language Standardization (Border radius: 12px, margin: 20px) */
        .glass-card, [data-testid="stForm"], [data-testid="stVerticalBlockBorder"] {
            background-color: #ffffff !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 12px !important; /* Standardized radius */
            padding: 32px !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03) !important;
            margin-bottom: 20px !important;
        }

        .job-card {
            background-color: #ffffff !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 12px !important; /* Standardized radius */
            padding: 24px !important;
            margin-bottom: 20px !important;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02) !important;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        .job-card:hover {
            border-color: #2563eb !important;
            box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.1) !important;
            transform: translateY(-2px) !important;
        }

        /* Inputs & Form controls standardized styling */
        input, select, textarea, [data-baseweb="input"], [data-baseweb="select"] {
            background-color: #ffffff !important;
            border: 1px solid #cbd5e1 !important;
            border-radius: 12px !important; /* Standardized radius */
            color: #0f172a !important;
            font-size: 0.95rem !important;
            padding: 10px 14px !important;
        }
        input::placeholder {
            color: #94a3b8 !important;
        }
        
        /* Modernized and Polished File Uploader Zone */
        [data-testid="stFileUploader"] {
            background-color: #f8fafc !important;
            border: 2px dashed #3b82f6 !important;
            border-radius: 12px !important;
            padding: 32px !important;
            transition: all 0.2s ease-in-out !important;
        }
        [data-testid="stFileUploader"]:hover {
            background-color: #f1f5f9 !important;
            border-color: #2563eb !important;
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.05) !important;
        }
        [data-testid="stFileUploader"] * {
            color: #0f172a !important;
        }
        
        /* Button Components styling (Streamlit Form Buttons) */
        .stButton>button {
            background-color: #1e40af !important; /* High contrast primary */
            color: #ffffff !important;
            border: 2px solid #2563eb !important;
            border-radius: 12px !important; /* Standardized radius */
            font-weight: 800 !important;
            padding: 12px 28px !important;
            font-size: 0.95rem !important;
            text-transform: uppercase !important;
            letter-spacing: 0.5px !important;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #2563eb !important;
            border-color: #3b82f6 !important;
            transform: scale(1.005) !important;
            box-shadow: 0 8px 20px rgba(37, 99, 235, 0.35) !important;
        }
        .stButton>button:active {
            transform: scale(0.995) !important;
            box-shadow: 0 2px 6px rgba(37, 99, 235, 0.15) !important;
        }
        .stButton>button:disabled {
            background-color: #e2e8f0 !important;
            color: #94a3b8 !important;
            border-color: #cbd5e1 !important;
            cursor: not-allowed !important;
            box-shadow: none !important;
        }

        /* Custom HTML Button Classes for consistency */
        .btn-primary {
            background-color: #1e40af !important;
            color: #ffffff !important;
            border: 2px solid #2563eb !important;
            border-radius: 12px !important;
            font-weight: 800 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.5px !important;
            padding: 12px 24px !important;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
            width: 100%;
            display: block;
            text-align: center;
        }
        .btn-primary:hover {
            background-color: #2563eb !important;
            border-color: #3b82f6 !important;
            box-shadow: 0 8px 20px rgba(37, 99, 235, 0.35) !important;
        }
        .btn-primary:active {
            transform: scale(0.995) !important;
        }

        /* Badges styling */
        .badge {
            display: inline-block !important;
            padding: 4px 12px !important;
            border-radius: 4px !important;
            font-size: 0.75rem !important;
            font-weight: 600 !important;
            margin-right: 8px !important;
            margin-bottom: 8px !important;
            text-transform: uppercase !important;
            letter-spacing: 0.5px !important;
        }
        .badge-purple {
            background-color: #eff6ff !important;
            color: #1e40af !important;
            border: 1px solid #bfdbfe !important;
        }
        .badge-blue {
            background-color: #f8fafc !important;
            color: #475569 !important;
            border: 1px solid #cbd5e1 !important;
        }
        .badge-green {
            background-color: #ecfdf5 !important;
            color: #047857 !important;
            border: 1px solid #a7f3d0 !important;
        }

        /* Match Score display */
        .score-circle {
            font-size: 2.4rem !important;
            font-weight: 800 !important;
            color: #1e40af !important;
            text-align: right !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
