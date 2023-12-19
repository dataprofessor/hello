import streamlit as st
import streamlit.components.v1 as components
import requests

# Page title
st.set_page_config(page_title="Welcome to Streamlit",
                   page_icon="👋",
                   layout="wide")
st.title('Welcome to Streamlit 👋')

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'Page 1'
if 'btn_type' not in st.session_state:
    st.session_state.btn_type = 'primary'

def page1():
  st.session_state.page = 'Page 1'
  st.session_state.btn_type = 'primary'

# Read app from GitHub repo
def read_gh(input_url):
  return requests.get(input_url).text

# CSS styling
st.markdown("""
<style>

[data-testid="block-container"] {
    padding-top: 1.3rem;
    padding-bottom: -5rem;

.st-emotion-cache-1b2gb7x.e1ycw9pz3, .st-emotion-cache-keje6w.e1f1d6gn3, .div.code.language-python {
    height: 380px;
}

</style>
""", unsafe_allow_html=True)

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
  btn1 = st.button('**Your Streamlit AI Assistant**', on_click=page1, type=st.session_state.btn_type)
with col[1]:
  btn2 = st.button('**Your LLM Playground**')
with col[2]:
  btn3 = st.button('**Exploratory Data Analysis**')
with col[3]:
  btn4 = st.button('**Build your ML Model**')

# Display page content
if st.session_state.page == 'Page 1':
  col1 = st.columns(2)
  with col1[0]:
    with st.container():
      st.code(read_gh('https://raw.githubusercontent.com/dataprofessor/builder/master/streamlit_app.py'), line_numbers=True)
  with col1[1]:
    app1 = 'https://builder.streamlit.app'
    st.components.v1.html(f"""<iframe src="{app1}/?embed=true" height=380 style="width:100%;border:none;"></iframe>""", width=None, height=1200, scrolling=False)



