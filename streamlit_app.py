import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sidebar
st.sidebar.title("This is my sidebar")
st.sidebar.button("You can click this, but it does not do anything")
sidebar_option = st.sidebar.radio("What do you want to see?", ["All of the streamlit toys", "Some way to work with files"])

if sidebar_option == 'Some way to work with files':
  uploaded_file = st.file_uploader('Upload a CSV file to explore', type='csv')

  if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, header=0)
        df = df.set_index('source')

        # Create a pick list to pick which friuts they want
        sources_selected = st.multiselect('Select Source:', list(set(df.index)),['Fetch Rewards'])
        sources_to_show = df.loc[sources_selected]

        # Display the table on the page
        ## st.dataframe(sources_to_show)

        st.subheader("Find the Files You Would Like to Fix")
        st.experimental_data_editor(sources_to_show, num_rows="dynamic")
    except:
      st.error("The file did not match the expected input")

else:
  # Titles and text
  st.title ("this is the app title")
  st.header("this is the markdown")
  st.markdown("this is the header")
  st.subheader("this is the subheader")
  st.caption("this is the caption")
  st.code("x=2021")
  st.latex(r''' a+a r^1+a r^2+a r^3 ''')
  
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
  
  st.subheader("Make 3 good choices for a surprise!")
  col1, col2, col3 = st.columns(3)
  
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


