import streamlit as st

st.set_page_config(layout="wide")

pg = st.navigation([
    st.Page('Pages/home.py', title='Home', icon='🏠', url_path='home'),
    st.Page('Pages/countries.py', title='Countries', icon='🌎', url_path='countries'),
    st.Page('Pages/cities.py', title='Cities', icon='🏙️', url_path='cities'),
    st.Page('Pages/cuisines.py', title='Cuisines', icon='🍽️', url_path='cuisines'),
])


pg.run()