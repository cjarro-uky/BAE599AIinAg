import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('C:\\Users\\caja222\\OneDrive - University of Kentucky\\Documents\\BAE599 - AI in Ag\\CornDB\\Cropland Value.csv')

# Convert Value column from string to numeric, removing $ and commas
df['Value'] = df['Value'].str.replace('$', '').str.replace(',', '').astype(float)

# Create the plot
plt.figure(figsize=(12, 6))

# Plot line for each state
for state in ['KENTUCKY', 'INDIANA', 'OHIO', 'TENNESSEE']:
    state_data = df[df['State'] == state]
    plt.plot(state_data['Year'], state_data['Value'], marker='o', label=state)

# Customize the plot
plt.title('Cropland Value per Acre (1997-2025)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Value ($/acre)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Display the plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('C:\\Users\\caja222\\OneDrive - University of Kentucky\\Documents\\BAE599 - AI in Ag\\CornDB\\PriceReceived.csv')

# Create the plot
plt.figure(figsize=(12, 6))

# Plot the price index
plt.plot(df['Year'], df['Value'], marker='o', label='Food Commodities', color='blue')

# Customize the plot
plt.title('National Index of Price Received (1990-2024)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Price Index (2011 = 100)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Display the plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('C:\\Users\\caja222\\OneDrive - University of Kentucky\\Documents\\BAE599 - AI in Ag\\CornDB\\Crop Prices.csv')

# Create the plot
plt.figure(figsize=(12, 6))

# Plot line for each commodity
for commodity in ['CORN', 'SOYBEANS', 'WHEAT']:
    commodity_data = df[df['Commodity'] == commodity]
    plt.plot(commodity_data['Year'], commodity_data['Value'], marker='o', label=commodity.capitalize())

# Customize the plot
plt.title('National Crop Prices (1975-2024)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Price ($/bushel)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Display the plot
plt.show()