import sys
import matplotlib
import pandas as pd
import mpl_toolkits  # needed for the map of the usa
import geopandas as gp
# we care only about the make and the zip code from the xlsx sheet, we are also including the price
cols = [6, 8, 13]
brandname = "Honda"
df = pd.read_excel("hz.xlsx", usecols=cols, converters={
    'Zipcode': lambda x: str(x), 'Price': lambda y: int(y[19:].replace(",", ""))})  # trim off the excess from the price column
df_honda = df[df['Make'] == "Honda"]
print(df_honda.keys())
df_honda_median = df_honda.groupby("Zipcode", as_index=False).median()
print(df_honda_median["Zipcode"].shape)
zip_code_boundaries = gp.read_file("tl_2018_us_zcta510.shp")
print(zip_code_boundaries['ZCTA5CE10'])
print(zip_code_boundaries['GEOID10'])
print(zip_code_boundaries['MTFCC10'])
print(zip_code_boundaries['ALAND10'])
print(zip_code_boundaries['AWATER10'])
print(zip_code_boundaries['INTPTLAT10'])
print(zip_code_boundaries['INTPTLON10'])
print(zip_code_boundaries['geometry'][::2])
showObj = zip_code_boundaries.plot()

matplotlib.pyplot.show()
