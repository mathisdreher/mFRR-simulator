import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Display Logo
logo = 'https://www.flexcity.energy/sites/g/files/dvc3216/files/Logo-Flexcity-by-Veolia---480x128.jpg'  # Update this with the path to the Flexcity logo you downloaded
st.image(logo, width=300)

# Title
st.title('MFRR Revenue Simulator for Flexcity')

# User Inputs
volume_MWh = st.number_input('Enter the volume in MW/h:', min_value=0)
selection_rate = st.slider('Selection Rate (%)', 80, 90, 85)
price_per_MWh = st.slider('Price per MW/h (€)', 8, 12, 9)
activation_payment = st.slider('Activation Payment (€/MWh)', 1200, 1800, 1500)
activation_rate = st.slider('Activation Rate (%)', 0.02, 0.03, 0.025)

# Calculations
annual_availability_revenue = volume_MWh * price_per_MWh * (selection_rate / 100)
annual_activation_revenue = volume_MWh * activation_payment * (activation_rate / 100)

# Displaying the Results
st.write('### Annual Availability Revenue')
st.write(f'€ {annual_availability_revenue:.2f}')

st.write('### Annual Activation Revenue')
st.write(f'€ {annual_activation_revenue:.2f}')

# Graph
fig, ax = plt.subplots()
revenue_types = ['Availability', 'Activation']
revenues = [annual_availability_revenue, annual_activation_revenue]
ax.bar(revenue_types, revenues, color=['blue', 'green'])
ax.set_ylabel('Revenue (€)')
ax.set_title('Revenue Comparison')
st.pyplot(fig)
