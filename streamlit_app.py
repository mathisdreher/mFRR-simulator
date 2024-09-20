import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Display Logo
logo = 'https://www.flexcity.energy/sites/g/files/dvc3216/files/Logo-Flexcity-by-Veolia---480x128.jpg'
st.image(logo, width=300)

# Title
st.title('MFRR Revenue Simulator for Flexcity')

# Constants
total_hours_per_year = 8760
total_days_per_year = 365
hours_per_activation = 4

# User Inputs
capacity_MW = st.number_input('Enter the capacity in MW:', min_value=1.0, step=0.1)
selection_rate = st.slider('Selection Rate (%)', 80, 90, 85)
price_per_MW_per_hour = round(st.slider('Availability Payment Rate (€/MW/h)', 6.0, 12.0, 9.0),1)
activation_payment_per_MWh = st.slider('Activation Payment (€/MWh)', 1200, 1800, 1500)
activations = round(st.slider('Activations days', 1.0, 6.0, 2.5, format="%.1f"),1)

# Calculations for MFRR
annual_availability_revenue = capacity_MW * price_per_MW_per_hour * total_hours_per_year * (selection_rate / 100)
annual_activation_revenue = capacity_MW * activation_payment_per_MWh * hours_per_activation * activations
total_revenue = annual_availability_revenue + annual_activation_revenue


# Dynamic Display for MFRR with
st.markdown(f"### With :red[{capacity_MW} MW] of flex capacity, you could earn :red[€{total_revenue:,.0f}] based on :red[assumptions] with Flexcity.")

# Pie Chart for MFRR Revenue Mix
labels = ['Availability Revenue', 'Activation Revenue']
sizes = [annual_availability_revenue, annual_activation_revenue]
colors = ['#1f77b4', '#b41f1f']
explode = (0.1, 0)  # explode the 1st slice (Availability Revenue)

# Format the labels to show both the name and the value
formatted_labels = [f'{label}: €{size:,.1f}' for label, size in zip(labels, sizes)]

# Plotting the pie chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=formatted_labels, colors=colors, autopct='%1.1f%%',
        shadow=False, startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)

# CTA
st.markdown("""
**Next Steps:**
- Customize the assumptions to reflect your specific expectations.
- Contact Flexcity for a personalized consultation and to learn how we can help you optimize your battery's performance.
""")
