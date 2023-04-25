import streamlit as st

def landing():
    st.sidebar.title('Contents')
    # st.sidebar.write('Please select a page :point_down:')
    add_selectbox = st.sidebar.radio(
                                        "",
                                        (
                                        "Introduction",
                                        "Exploratory Data Analysis",
                                        "Feature Engineering",
                                        # "Prediction Models"
                                        )
                                    )
    return add_selectbox