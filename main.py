import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px
import streamlit as st



data=pd.read_csv("ds_salaries.csv")
locations = [ 'IN','DE', 'SG']

# Filter the DataFrame based on whether the 'company_location' column value is in the list
filtered_data = data[data['company_location'].isin(locations)]
if 3574 in filtered_data.index:
    filtered_data=filtered_data.drop([3574], inplace=True)
else:
    print("Index 3574 not found in the DataFrame")

india_data=filtered_data.loc[filtered_data["company_location"]=="IN"].groupby("work_year").agg({"salary_in_usd":["mean"]})
singapore_data=filtered_data.loc[filtered_data["company_location"]=="SG"].groupby("work_year").agg({"salary_in_usd":["mean"]})
germany_data=filtered_data.loc[filtered_data["company_location"]=="DE"].groupby("work_year").agg({"salary_in_usd":["mean"]})
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed

country_mapping = {
    'ES': 'ESP',  # Spain
    'US': 'USA',  # United States
    'CA': 'CAN',  # Canada
    'DE': 'DEU',  # Germany
    'GB': 'GBR',  # United Kingdom
    'NG': 'NGA',  # Nigeria
    'IN': 'IND',  # India
    'HK': 'HKG',  # Hong Kong
    'NL': 'NLD',  # Netherlands
    'CH': 'CHE',  # Switzerland
    'CF': 'CAF',  # Central African Republic
    'FR': 'FRA',  # France
    'FI': 'FIN',  # Finland
    'UA': 'UKR',  # Ukraine
    'IE': 'IRL',  # Ireland
    'IL': 'ISR',  # Israel
    'GH': 'GHA',  # Ghana
    'CO': 'COL',  # Colombia
    'SG': 'SGP',  # Singapore
    'AU': 'AUS',  # Australia
    'SE': 'SWE',  # Sweden
    'SI': 'SVN',  # Slovenia
    'MX': 'MEX',  # Mexico
    'BR': 'BRA',  # Brazil
    'PT': 'PRT',  # Portugal
    'RU': 'RUS',  # Russia
    'TH': 'THA',  # Thailand
    'HR': 'HRV',  # Croatia
    'VN': 'VNM',  # Vietnam
    'EE': 'EST',  # Estonia
    'AM': 'ARM',  # Armenia
    'BA': 'BIH',  # Bosnia and Herzegovina
    'KE': 'KEN',  # Kenya
    'GR': 'GRC',  # Greece
    'MK': 'MKD',  # North Macedonia
    'LV': 'LVA',  # Latvia
    'RO': 'ROU',  # Romania
    'PK': 'PAK',  # Pakistan
    'IT': 'ITA',  # Italy
    'MA': 'MAR',  # Morocco
    'PL': 'POL',  # Poland
    'AL': 'ALB',  # Albania
    'AR': 'ARG',  # Argentina
    'LT': 'LTU',  # Lithuania
    'AS': 'ASM',  # American Samoa
    'CR': 'CRI',  # Costa Rica
    'IR': 'IRN',  # Iran
    'BS': 'BHS',  # Bahamas
    'HU': 'HUN',  # Hungary
    'AT': 'AUT',  # Austria
    'SK': 'SVK',  # Slovakia
    'CZ': 'CZE',  # Czech Republic
    'TR': 'TUR',  # Turkey
    'PR': 'PRI',  # Puerto Rico
    'DK': 'DNK',  # Denmark
    'BO': 'BOL',  # Bolivia
    'PH': 'PHL',  # Philippines
    'BE': 'BEL',  # Belgium
    'ID': 'IDN',  # Indonesia
    'EG': 'EGY',  # Egypt
    'AE': 'ARE',  # United Arab Emirates
    'LU': 'LUX',  # Luxembourg
    'MY': 'MYS',  # Malaysia
    'HN': 'HND',  # Honduras
    'JP': 'JPN',  # Japan
    'DZ': 'DZA',  # Algeria
    'IQ': 'IRQ',  # Iraq
    'CN': 'CHN',  # China
    'NZ': 'NZL',  # New Zealand
    'CL': 'CHL',  # Chile
    'MD': 'MDA',  # Moldova
    'MT': 'MLT'  # Malta
}


def country(con):
    return country_mapping[con]


data["iso3 alpha"] = data["company_location"].apply(country)
mean_salaries = data.groupby('iso3 alpha')['salary_in_usd'].mean().reset_index()
# Create a choropleth map using Plotly
fig = px.choropleth(
    mean_salaries,
    locations='iso3 alpha',         # DataFrame column with ISO Alpha-3 codes
    color='salary_in_usd',         # DataFrame column with color values
    hover_name='iso3 alpha',  # DataFrame column to add to hover information
    locationmode='ISO-3',           # Set to plot based on ISO Alpha-3 codes
    color_continuous_scale='Plasma',  # Color scale
    range_color=(0, mean_salaries['salary_in_usd'].max()),  # Range of color scale
    title='Mean Salary by Country'  # Title of the plot
)

# Show the plot

st.title('Streamlit Plotly Dashboard')
st.write("Here's a Plotly line plot:")
st.plotly_chart(fig)

