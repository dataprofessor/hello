import streamlit as st

# Font awesome icon
st.markdown('''
  i {
    color: #FFFFFF;
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
  st.markdown(f'<style>{css_styles}</style>', unsafe_allow_html=True)
      
  
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
  
  <p align="center">
      <span style="color: #FFBD45;">Follow:</span>&nbsp;
      <a href="https://github.com/streamlit"><i class="fab fa-github"></i></a>
      <a href="https://twitter.com/streamlit/"><i class="fa-brands fa-x-twitter"></i></a>
      <a href="https://www.linkedin.com/company/streamlit/"><i class="fab fa-linkedin-in"></i></a>
      <a href="https://www.youtube.com/@streamlitofficial"><i class="fab fa-youtube"></i></a>
      <a href="https://www.instagram.com/streamlit.io/"><i class="fab fa-instagram"></i></a>
  </p>
''', unsafe_allow_html=True)
