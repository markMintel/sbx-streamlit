import streamlit as st

st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

show_image = st.checkbox("Show Image")
if show_image:
  st.image("streamlit_tp.png")
