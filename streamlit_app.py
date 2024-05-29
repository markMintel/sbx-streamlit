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

st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

#st.progress(i*10)
if my_mark == 'Excellent' and my_number == 1:
  with st.spinner('Wait for it...'):    
    time.sleep(5)
  st.balloons()

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

with st.popover("Settings"):
  st.checkbox("I'm done here")
