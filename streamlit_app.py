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
volume_MWh = st.number_input('Enter the volume in MW/h:', min_value=0,step=0.1)
selection_rate = st.slider('Selection Rate (%)', 80, 90, 85)
price_per_MWh = st.slider('Price per MW/h (€)', 6, 12, 9)
activation_payment = st.slider('Activation Payment (€/MWh)', 1200, 1800, 1500)
activation_rate = st.slider('Activation Rate (‰)', 0.2, 0.3, 0.25)

# Calculations for MFRR
annual_availability_revenue = volume_MWh * price_per_MWh * (selection_rate / 100)
annual_activation_revenue = volume_MWh * activation_payment * (activation_rate / 100)
total_revenue = annual_availability_revenue + annual_activation_revenue

# Number of activation days (assuming one activation per day)
activation_days = activation_rate * 365

# Dynamic Display for MFRR
st.markdown(f"### With **{volume_MWh} MW** of flex capacity, you could earn **€{total_revenue:.2f}** based on an assumption of **{activation_days:.1f} activation days** per year with Flexcity.")

# Pie Chart for MFRR Revenue Mix
labels = ['Availability Revenue', 'Activation Revenue']
sizes = [annual_availability_revenue, annual_activation_revenue]
colors = ['#1f77b4', '#ff7f0e']
explode = (0.1, 0)  # explode the 1st slice (Availability Revenue)

# CTA
st.markdown("""
**Next Steps:**
- Customize the assumptions to reflect your specific expectations.
- Contact Flexcity for a personalized consultation and to learn how we can help you optimize your battery's performance.
""")
