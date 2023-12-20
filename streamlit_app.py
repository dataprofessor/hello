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
if 'btn1_type' not in st.session_state:
    st.session_state.btn1_type = 'primary'
if 'btn2_type' not in st.session_state:
    st.session_state.btn2_type = 'secondary'
if 'btn3_type' not in st.session_state:
    st.session_state.btn3_type = 'secondary'
if 'btn4_type' not in st.session_state:
    st.session_state.btn4_type = 'secondary'

# Custom functions
## Button types
def page1():
  st.session_state.page = 'Page 1'
  st.session_state.btn1_type = 'primary'
  st.session_state.btn2_type = 'secondary'
  st.session_state.btn3_type = 'secondary'
  st.session_state.btn4_type = 'secondary'

def page2():
  st.session_state.page = 'Page 2'
  st.session_state.btn1_type = 'secondary'
  st.session_state.btn2_type = 'primary'
  st.session_state.btn3_type = 'secondary'
  st.session_state.btn4_type = 'secondary'

def page3():
  st.session_state.page = 'Page 3'
  st.session_state.btn1_type = 'secondary'
  st.session_state.btn2_type = 'secondary'
  st.session_state.btn3_type = 'primary'
  st.session_state.btn4_type = 'secondary'

def page4():
  st.session_state.page = 'Page 4'
  st.session_state.btn1_type = 'secondary'
  st.session_state.btn2_type = 'secondary'
  st.session_state.btn3_type = 'secondary'
  st.session_state.btn4_type = 'primary'

## Load app page
@st.cache_resource
def app_page(input_url):
  return st.components.v1.html(f'''<iframe src="{input_url}/?embed=true" height=420 style="width:100%;border:none;"></iframe>''', width=None, height=420, scrolling=False)

## Read app from GitHub repo
def read_gh(input_url):
  return requests.get(input_url).text


# CSS styling
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


st.write(f"I was built with {app_code.count('\n')} lines of code. It is wicked easy!")
with st.expander("Expand to see this app's code"):
  app_code = read_gh('https://raw.githubusercontent.com/dataprofessor/hello/master/streamlit_app.py')
  st.code(app_code, line_numbers=True)

st.header('What would you like to build?', divider=True)

col = st.columns(4)
with col[0]:
  btn1 = st.button('**Your Streamlit AI Assistant**', on_click=page1, type=st.session_state.btn1_type)
with col[1]:
  btn2 = st.button('**Your LLM Playground**', on_click=page2, type=st.session_state.btn2_type)
with col[2]:
  btn3 = st.button('**Exploratory Data Analysis**', on_click=page3, type=st.session_state.btn3_type)
with col[3]:
  btn4 = st.button('**Build your ML Model**', on_click=page4, type=st.session_state.btn4_type)

# Display page content
if st.session_state.page == 'Page 1':
  col1 = st.columns(2)
  with col1[0]:
    with st.container():
      st.code(read_gh('https://raw.githubusercontent.com/dataprofessor/builder/master/streamlit_app.py'), line_numbers=True)
  with col1[1]:
    app1 = 'https://builder.streamlit.app'
    app_page(app1)
    # st.components.v1.html(f'''<iframe src="{app1}/?embed=true" height=420 style="width:100%;border:none;"></iframe>''', width=None, height=420, scrolling=False)

if st.session_state.page == 'Page 2':
  col2 = st.columns(2)
  with col2[0]:
    with st.container():
      st.code(read_gh('https://raw.githubusercontent.com/streamlit/llm-examples/main/Chatbot.py'), line_numbers=True)
  with col2[1]:
    app2 = 'https://llm-examples.streamlit.app'
    app_page(app2)
    # st.components.v1.html(f'''<iframe src="{app2}/?embed=true" height=420 style="width:100%;border:none;"></iframe>''', width=None, height=420, scrolling=False)

if st.session_state.page == 'Page 3':
  col3 = st.columns(2)
  with col3[0]:
    with st.container():
      st.code(read_gh('https://raw.githubusercontent.com/dataprofessor/movies-explorer/master/streamlit_app.py'), line_numbers=True)
  with col3[1]:
    app3 = 'https://movies-explorer.streamlit.app'
    app_page(app3)

if st.session_state.page == 'Page 4':
  col4 = st.columns(2)
  with col4[0]:
    with st.container():
      st.code(read_gh('https://raw.githubusercontent.com/dataprofessor/ml-app-v2/master/streamlit_app.py'), line_numbers=True)
  with col4[1]:
    app4 = 'https://ml-app-v2.streamlit.app/'
    app_page(app4)
