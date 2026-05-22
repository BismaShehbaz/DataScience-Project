import streamlit as st
import time

# Page Config - Must be first Streamlit command
st.set_page_config(
    page_title="VisionLink: AI Welcome", 
    page_icon="🎓", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Next-Level UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    /* Main Background & Fonts */
    .stApp {
        background: #0f172a;
        background-image: 
            radial-gradient(at 0% 0%, hsla(253,16%,7%,1) 0, transparent 50%), 
            radial-gradient(at 50% 0%, hsla(225,39%,30%,0.2) 0, transparent 50%), 
            radial-gradient(at 100% 0%, hsla(339,49%,30%,0.2) 0, transparent 50%);
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #f8fafc;
    }

    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Welcome Screen Styles */
    .welcome-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 70vh;
        text-align: center;
        animation: fadeIn 1s ease-out forwards;
    }
    
    .welcome-icon {
        font-size: 8rem;
        margin-bottom: 1rem;
        animation: pulse 2s infinite;
    }
    
    .welcome-title {
        font-size: 5rem;
        font-weight: 800;
        background: linear-gradient(to right, #38bdf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .welcome-subtitle {
        font-size: 1.5rem;
        color: #94a3b8;
        max-width: 600px;
        margin-bottom: 3rem;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    div.stButton > button {
        border-radius: 16px;
        font-size: 1.3rem;
        font-weight: 700;
        letter-spacing: 2px;
        padding: 1rem 0px;
        background: linear-gradient(135deg, #0ea5e9, #8b5cf6, #d946ef);
        background-size: 200% auto;
        color: white !important;
        border: none;
        box-shadow: 0 10px 25px -5px rgba(139, 92, 246, 0.5);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        text-transform: uppercase;
    }
    
    div.stButton > button:hover {
        background-position: right center;
        transform: translateY(-4px);
        box-shadow: 0 15px 35px -5px rgba(139, 92, 246, 0.7);
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="welcome-container">
    <div class="welcome-icon">🎓</div>
    <div class="welcome-title">VisionLink AI</div>
    <div class="welcome-subtitle">Empowering Visually Impaired Students through Predictive Machine Learning Analytics.</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("Launch AI Platform", type="primary", use_container_width=True):
        st.switch_page("pages/1_Dashboard.py")
