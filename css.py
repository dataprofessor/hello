import streamlit as st

def load_css():
  # Page syling
  st.markdown("""
    <style>
    
    [data-testid="block-container"] {
        padding-top: 1.5rem;
        padding-bottom: 1.5rem;
    }
    
    .st-emotion-cache-1b2gb7x.e1ycw9pz3 {
        padding-top: 10px;
        height: 420px;
    }
    </style>
  """, unsafe_allow_html=True)
  
