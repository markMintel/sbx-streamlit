import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np


# Titles and text
st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# Sidebar
st.sidebar.title("This is my sidebar")
st.sidebar.button("You can click this, but it does not do anything")
st.sidebar.radio("Is this useful?", ["Yes it is", "Maybe, I don't quite know yet"])

# Images
show_image = st.checkbox("Show Image")
if show_image:
  st.image("streamlit_tp.png")

# User input tools
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
my_mark = st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
my_number = st.slider('Pick a number', 0,50)

#st.progress(i*10)
if my_mark == 'Excellent' and my_number == 1:
  with st.spinner('Wait for it...'):    
    time.sleep(5)
  st.balloons()

st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

# Messages
st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

# Containers
container = st.container()
container.write("Here is some text in my container")

st.write("This text is not inside the container")

# Displaying graphs
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)


col1, col2, col3 = st.columns(3)
st.subheader("Make 3 good choices for a surprise!")
with col1:
  with st.popover("Choice 1"):
    gc1 = st.checkbox("Good Choice 1")
    bc1 = st.checkbox("Bad Choice 1")

with col2:
  with st.popover("Choice 2"):
    gc2 = st.checkbox("Good Choice 2")
    bc2 = st.checkbox("Bad Choice 2")

with col3:
  with st.popover("Choice"):
    gc3 = st.checkbox("Good Choice 3")
    bc3 = st.checkbox("Bad Choice 3")

if gc1 and gc2 and gc3:
  st.balloons()

if bc1 and bc2 and bc3:
  st.error("3 bad choices? Please reconsider")


