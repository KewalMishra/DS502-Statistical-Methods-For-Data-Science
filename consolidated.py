import streamlit as st

from intro_page import intro
from eda_page import eda
from feat_engg_page import feature_engineering
from pred_model_page import prediction_models
from landing_page import landing

add_selectbox = landing()

if add_selectbox=='Introduction': intro()
if add_selectbox=='Exploratory Data Analysis': eda()
if add_selectbox=='Feature Engineering': feature_engineering()
if add_selectbox=='Prediction Models': prediction_models()