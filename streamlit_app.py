import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Display Logo
logo = 'https://www.flexcity.energy/sites/g/files/dvc3216/files/Logo-Flexcity-by-Veolia---480x128.jpg'
st.image(logo, width=300)

# Title
st.title('MFRR Revenue Simulator for Flexcity')

# User Inputs
capacity_MW = st.number_input('Enter the capacity in MW:', min_value=1.0, step=0.1)
selection_rate = st.slider('Selection Rate (%)', 80, 90, 85)
price_per_MW_per_hour = st.slider('Availability Payment Rate (€/MW/h)', 6, 12, 9)
activation_payment_per_MWh = st.slider('Activation Payment (€/MWh)', 1200, 1800, 1500)
activation_rate = st.slider('Activation Rate (‰)', 0.2, 0.3, 0.25)

# Constants
total_hours_per_year = 8760

# Calculations for MFRR
annual_availability_revenue = capacity_MW * price_per_MW_per_hour * total_hours_per_year * (selection_rate / 100)
annual_activation_revenue = capacity_MW * activation_payment_per_MWh * total_hours_per_year * (activation_rate / 1000)
total_revenue = annual_availability_revenue + annual_activation_revenue

# Number of activation hours per year
activation_hours_per_year = total_hours_per_year * (activation_rate / 1000)

# Dynamic Display for MFRR
st.markdown(f"### With red:[**{capacity_MW} MW**] of flex capacity, you could earn red:[**€{total_revenue:,.2f}** based on an assumption of red:[**{activation_hours_per_year:.1f} activation hours**] per year with Flexcity.")

# Pie Chart for MFRR Revenue Mix
labels = ['Availability Revenue', 'Activation Revenue']
sizes = [annual_availability_revenue, annual_activation_revenue]
colors = ['#1f77b4', '#ff7f0e']
explode = (0.1, 0)  # explode the 1st slice (Availability Revenue)

# Plotting the pie chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)

# CTA
st.markdown("""
    ### Understanding the Business Case

    Participating in the mFRR market can provide significant revenue streams.
    By partnering with Flexcity, you can maximize your asset potential through expert market access and optimized operations.

    - **Capacity Revenue:** Earnings from being available to provide mFRR services.
    - **Activation Revenue:** Earnings from actual energy delivery during activations.


    ### Next Steps

    - **Customize Assumptions:** Adjust the parameters to reflect your expectations.
    - **Contact Flexcity:** [Get in touch](https://www.flexcity.energy/contact) for a personalized consultation.

""")
