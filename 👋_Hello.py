import streamlit as st
import streamlit.components.v1 as components
import requests
import css

# Page title
st.set_page_config(page_title="Welcome to Streamlit",
                   page_icon="👋",
                   layout="wide")
st.title('Welcome to Streamlit 👋')

# Sidebar
#with st.sidebar:
  

## Load app page
@st.cache_resource
def app_page(input_url):
  return st.components.v1.html(f'''<iframe src="{input_url}/?embed=true" height=420 style="width:100%;border:none;"></iframe>''', width=None, height=420, scrolling=False)

## Read app from GitHub repo
def read_gh(input_url):
  return requests.get(input_url).text

# Page description
app_code = read_gh('https://raw.githubusercontent.com/dataprofessor/hello/master/streamlit_app.py')
app_line_count = app_code.count('\n')

with st.expander(f"I was built in {app_line_count} lines of code, expand here to see"):
  st.code(app_code, line_numbers=True)

st.header('What would you like to build?', divider=True)
st.info('A faster way to build interactive data apps with just a few lines of code!')

tab = st.tabs(['Your Streamlit AI Assistant',
                                 'Exploratory Data Analysis',
                                 'Build your ML Model',
                                 'Support Ticket Workflow']
                                )

# Display page content
with tab[0]:
  col1 = st.columns(2)
  with col1[0]:
    with st.container():
      st.code(read_gh('https://raw.githubusercontent.com/dataprofessor/builder/master/streamlit_app.py'), line_numbers=True)
  with col1[1]:
    app1 = 'https://builder.streamlit.app'
    app_page(app1)
    # st.components.v1.html(f'''<iframe src="{app1}/?embed=true" height=420 style="width:100%;border:none;"></iframe>''', width=None, height=420, scrolling=False)

with tab[1]:
  col2 = st.columns(2)
  with col2[0]:
    with st.container():
      st.code(read_gh('https://raw.githubusercontent.com/dataprofessor/movies-explorer/master/streamlit_app.py'), line_numbers=True)
  with col2[1]:
    app2 = 'https://movies-explorer.streamlit.app'
    app_page(app2)

with tab[2]:
  col3 = st.columns(2)
  with col3[0]:
    with st.container():
      st.code(read_gh('https://raw.githubusercontent.com/dataprofessor/machinelearning-app/master/streamlit_app.py'), line_numbers=True)
  with col3[1]:
    app3 = 'https://machinelearning1.streamlit.app/'
    app_page(app3)

with tab[3]:
  col4 = st.columns(2)
  with col4[0]:
    with st.container():
      st.code(read_gh('https://raw.githubusercontent.com/dataprofessor/support-ticket-workflow/master/streamlit_app.py'), line_numbers=True)
  with col4[1]:
    app4 = 'https://support-ticket-workflow.streamlit.app/'
    app_page(app4)
