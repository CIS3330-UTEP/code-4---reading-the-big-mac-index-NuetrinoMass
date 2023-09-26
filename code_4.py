import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    bmf = pd.read_csv(big_mac_file)
    bmf['year'] = pd.DatetimeIndex(bmf['date']).year
    bmf_sub = bmf[(bmf['year'] == year)& (bmf['iso_a3'] == country_code.upper())]
    return(bmf_sub['dollar_price'].mean().round(2))

def get_big_mac_price_by_country(country_code):
    bmf = pd.read_csv(big_mac_file)
    bmf_sub = bmf[(bmf['iso_a3'] == country_code.upper())]
    return(bmf_sub['dollar_price'].mean().round(2))

def get_the_cheapest_big_mac_price_by_year(year):
    bmf = pd.read_csv(big_mac_file)
    bmf['year'] = pd.DatetimeIndex(bmf['date']).year
    bmf_sub = (bmf[(bmf['year'] == year)])
    local = bmf_sub['dollar_price'].idxmin()
    ser = (bmf_sub.loc[local])
    name = ser.iloc[bmf_sub.columns.get_loc('name')]
    dp = round(ser.iloc[bmf_sub.columns.get_loc('dollar_price')],2)
    con= ser.iloc[bmf_sub.columns.get_loc('iso_a3')]
    x = f"{name}({con}): ${dp}"
    return(x)

def get_the_most_expensive_big_mac_price_by_year(year):
    bmf = pd.read_csv(big_mac_file)
    bmf['year'] = pd.DatetimeIndex(bmf['date']).year
    bmf_sub = (bmf[(bmf['year'] == year)])
    local = bmf_sub['dollar_price'].idxmax()
    ser = (bmf_sub.loc[local])
    name = ser.iloc[bmf_sub.columns.get_loc('name')]
    dp = round(ser.iloc[bmf_sub.columns.get_loc('dollar_price')],2)
    con= ser.iloc[bmf_sub.columns.get_loc('iso_a3')]
    x = f"{name}({con}): ${dp}"
    print(x)
    return(x)

if __name__ == "__main__":
    get_big_mac_price_by_year(2018,'usa')
    get_big_mac_price_by_country('rus')
    get_the_cheapest_big_mac_price_by_year(2008)
    get_the_most_expensive_big_mac_price_by_year(2016)
    pass # Remove this line and code your user interface