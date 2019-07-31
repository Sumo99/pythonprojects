import sys
import getopt
import matplotlib
import pandas as pd
import geopandas as gp
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt

# we care only about the make and the zip code from the xlsx sheet, we are also including the price
cols = [6, 8, 13]
# this the range of zip for each state, for example 99501 to 99950 belong to alaska
"""state_zip_ranges = {
    "AK": (99501, 99950),
    "AL": (35004, 36925),
    "AR": (71601, 72959)(75502, 75502),
    "AZ": (85001, 86556),
    "CA": (90001, 96162),
    "CO": (80001, 81658),
    "CT": (6001, 6389)(6401, 6928),
    "DE": (19701, 19980),
    "FL": (32004, 34997),
    "GA": (30001, 31999)(39901, 39901),
    "HI": (96701, 96898),
    "IA": (50001, 52809)(68119, 68120),
    "ID": (83201, 83876),
    "IL": (60001, 62999),
    "IN": (46001, 47997),
    "KS": (66002, 67954),
    "KY": (40003, 42788),
    "LA": (70001, 71232)(71234, 71497),
    "MA": (1001, 2791)()
}"""
with open("alaska.shp", "w+") as test_out:

    pass
geometry_set = []  # the set of polygons that have our cars prices in them
args = '-year -make -model -state -price -mileage -body -drive'.split()
print("The args is "+str(sys.argv))
brandname = sys.argv[1]  # the brandname is the first argument
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_excel("http://powerhi.com/html/files/hz.xlsx", usecols=cols, converters={
    'Zipcode': lambda x: str(x), 'Price': lambda y: int(y[19:].replace(",", ""))})  # trim off the excess from the price column
df_honda = df[df['Make'] == "Toyota"]
print(df_honda.keys())
df_honda_median = df_honda.groupby("Zipcode", as_index=False).min()
print(df_honda_median.head())
zip_code_boundaries = gp.read_file(
    "tl_2018_us_zcta510.shp")
zip_code_boundaries = zip_code_boundaries.rename(
    columns={"ZCTA5CE10": 'Zipcode'})
print(zip_code_boundaries.dtypes)
# zip_code_boundaries_ak = df[zip_code_boundaries['Zipcode'].astype(
#   str).astype(int)]
# print(zip_code_boundaries_ak.dtypes)
# gdf_ak = GeoDataFrame(zip_code_boundaries_ak,
# geometry=zip_code_boundaries_ak["geometry"])
# gdf_ak.plot()
df_honda = df[df['Make'] == "Toyota"]

df_honda = pd.merge(df_honda, zip_code_boundaries, how="right", on="Zipcode")
print("The new data is ")
print(df_honda.head())
print(len(zip_code_boundaries))
print()
gdf = GeoDataFrame(df_honda, geometry=df_honda["geometry"])
showObj = gdf.plot(cmap='coolwarm', column='Price', legend=True,
                   facecolor='#4D4D4D', edgecolor='#B3B3B3')
showObj.set_axis_off()
showObj.axis("equal")
matplotlib.pyplot.show()
zip_code_boundaries = zip_code_boundaries.astype({"Zipcode":
                                                  str}).astype({"Zipcode": int})
zip_code_boundaries_ak = zip_code_boundaries[(
    zip_code_boundaries['Zipcode'] > 99501) & (zip_code_boundaries['Zipcode'] < 99950)]
print("Here is alaska ")
print(zip_code_boundaries_ak.head())
gdf = GeoDataFrame(zip_code_boundaries_ak,
                   geometry=zip_code_boundaries_ak["geometry"])
gdf.plot()
test_zip_1 = gp.read_file(
    "/home/sumo/Documents/us_state_zipfiles/tl_2016_01_place")
test_zip_2 = gp.read_file(
    "/home/sumo/Documents/us_state_zipfiles/shp_bdry_zip_code_tabulation_areas")
print(" The new Files")
print()
print(test_zip_1.head())
print("Another File ")
print(test_zip_2.head())
showObj = test_zip_1.plot()
matplotlib.pyplot.show()
showObj = test_zip_2.plot()
matplotlib.pyplot.show()
