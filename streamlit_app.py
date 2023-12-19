import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Welcome to Streamlit",
                   page_icon="👋",
                   layout="wide")

st.title('Welcome to Streamlit 👋')

st.write("I was built with # lines of code. It's wicked easy")
with st.expander('Expand to see my code'):
  code = '''
  import streamlit as st

  st.write('Hello world!')
  '''
  st.code(code)

st.header('What would you like to build?', divider=True)

col = st.columns(4)

with col[0]:
  btn1 = st.button('**Your Streamlit AI Assistant**')
with col[1]:
  btn2 = st.button('**Your LLM Playground**')
with col[2]:
  btn3 = st.button('**Exploratory Data Analysis**')
with col[3]:
  btn4 = st.button('**Build your ML Model**')

if btn1:
  col1 = st.columns(2)
  with col1[0]:
    st.code(code)
  with col1[1]:
    app1 = 'https://builder.streamlit.app'
    st.components.v1.html(f"""<iframe src="{app1}/?embed=true" height=350 style="width:100%;border:none;"></iframe>""", width=None, height=1200, scrolling=False)



