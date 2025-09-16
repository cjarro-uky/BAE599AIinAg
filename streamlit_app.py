import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Agricultural Data Analysis Dashboard')

# Read all CSV files
cropland_df = pd.read_csv('Cropland Value.csv')
price_received_df = pd.read_csv('PriceReceived.csv')
crop_prices_df = pd.read_csv('Crop Prices.csv')

# Clean cropland values
cropland_df['Value'] = cropland_df['Value'].str.replace('$', '').str.replace(',', '').astype(float)

# Sidebar controls
st.sidebar.header('Filters')

# Year range selector
all_years = sorted(list(set(cropland_df['Year'].tolist() + 
                          price_received_df['Year'].tolist() + 
                          crop_prices_df['Year'].tolist())))
year_range = st.sidebar.slider('Select Year Range',
                             min_value=min(all_years),
                             max_value=max(all_years),
                             value=(min(all_years), max(all_years)))

# State selector for cropland values
states = ['KENTUCKY', 'INDIANA', 'OHIO', 'TENNESSEE']
selected_states = st.sidebar.multiselect('Select States for Cropland Values',
                                       states,
                                       default=states)

# Commodity selector for crop prices
commodities = ['CORN', 'SOYBEANS', 'WHEAT']
selected_commodities = st.sidebar.multiselect('Select Commodities',
                                            commodities,
                                            default=commodities)

# Plot 1: Cropland Values
st.header('Cropland Value per Acre')
fig1, ax1 = plt.subplots(figsize=(12, 6))

for state in selected_states:
    state_data = cropland_df[cropland_df['State'] == state]
    state_data = state_data[(state_data['Year'] >= year_range[0]) & 
                           (state_data['Year'] <= year_range[1])]
    ax1.plot(state_data['Year'], state_data['Value'], marker='o', label=state)

ax1.set_title('Cropland Value per Acre', fontsize=14)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Value ($/acre)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend()
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig1)

# Plot 2: Price Received Index
st.header('National Index of Price Received')
fig2, ax2 = plt.subplots(figsize=(12, 6))

price_received_filtered = price_received_df[
    (price_received_df['Year'] >= year_range[0]) & 
    (price_received_df['Year'] <= year_range[1])
]
ax2.plot(price_received_filtered['Year'], 
         price_received_filtered['Value'], 
         marker='o', 
         label='Food Commodities', 
         color='blue')

ax2.set_title('National Index of Price Received', fontsize=14)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Price Index (2011 = 100)', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend()
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig2)

# Plot 3: Crop Prices
st.header('National Crop Prices')
fig3, ax3 = plt.subplots(figsize=(12, 6))

for commodity in selected_commodities:
    commodity_data = crop_prices_df[crop_prices_df['Commodity'] == commodity]
    commodity_data = commodity_data[
        (commodity_data['Year'] >= year_range[0]) & 
        (commodity_data['Year'] <= year_range[1])
    ]
    ax3.plot(commodity_data['Year'], 
             commodity_data['Value'], 
             marker='o', 
             label=commodity.capitalize())

ax3.set_title('National Crop Prices', fontsize=14)
ax3.set_xlabel('Year', fontsize=12)
ax3.set_ylabel('Price ($/bushel)', fontsize=12)
ax3.grid(True, linestyle='--', alpha=0.7)
ax3.legend()
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig3)
