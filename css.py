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
  
  # Social icons https://codepen.io/kpdushanmaduka/pen/jadeoO
  css_styles = '''
  i {
    color: #111111;
    letter-spacing: 9px;
    padding: 0.5cm 0cm 0.5cm 0cm;
    font-size: 20px;
    transition: all .2s ease-in-out;
  }
  
  i:hover {transform: scale(1.5);}
  
  .fa-github:hover {color: #B3B6B7;}
  .fa-instagram:hover {color: #c32aa3;}
  .fa-twitter:hover {color: #1da1f2;}
  .fa-linkedin-in:hover {color: #0a66c2;}
  .fa-youtube:hover {color: #ff0000;}
  '''
  st.sidebar.markdown(f'<style>{css_styles}</style>', unsafe_allow_html=True)
      
  # Font awesome icon
  fa_css = '''
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
  
  <p align="center">
      Tag us when you publish your app! <br>
      <a href="https://github.com/streamlit"><i class="fab fa-github"></i></a>
      <a href="https://twitter.com/streamlit/"><i class="fa-brands fa-x-twitter"></i></a>
      <a href="https://www.linkedin.com/company/streamlit/"><i class="fab fa-linkedin-in"></i></a>
      <a href="https://www.youtube.com/@streamlitofficial"><i class="fab fa-youtube"></i></a>
      <a href="https://www.instagram.com/streamlit.io/"><i class="fab fa-instagram"></i></a>
  </p>
  '''      

  st.sidebar.markdown(fa_css, unsafe_allow_html=True)
