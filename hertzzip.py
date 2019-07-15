import csv
import pandas as pd
import numpy as np
import xlrd
import xlsxwriter
import sys
from os.path import expanduser
home = expanduser("~/Documents")
if(len(sys.argv) == 1):
    print("My first argument is the zip code, my second argument is an excel file")
myLatLongDictionary = {}
ep_lat = 44.863838  # is hardcoded for now, will add command line ability later
ep_long = -93.430008
cols = [13]  # we care only about the zip on the hertz excel spreadsheet
with open('zipcode2.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        myLatLongDictionary = {row["Zipcode"]: row["Lat"] +
                               ","+row["Long"] for row in csv_reader}
df = pd.read_excel("hz.xlsx", usecols=cols, converters={
                   'Zipcode': lambda x: str(x)})


def Haversine(lat1, lon1, lat2, lon2, **kwarg):
    """
    This uses the ‘haversine’ formula to calculate the great-circle distance between two points – that is,
    the shortest distance over the earth’s surface – giving an ‘as-the-crow-flies’ distance between the points
    (ignoring any hills they fly over, of course!).
    Haversine
    formula:    a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
    c = 2 ⋅ atan2( √a, √(1−a) )
    d = R ⋅ c
    where   φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km);
    note that angles need to be in radians to pass to trig functions!
    """
    R = 6371.0088
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2) ** 2
    c = 2 * np.arctan2(a**0.5, (1-a)**0.5)
    d = R * c
    return round(d)


distList = []
for i in range(0, df.shape[0]):
    zipCode = str(df.at[i, "Zipcode"])
    if(len(zipCode) == 4):
        zipCode = "0"+zipCode
    latLongZip = myLatLongDictionary.get(zipCode).split(",")
    distList.append(Haversine(ep_lat, ep_long, float(
        latLongZip[0]), float(latLongZip[1])))

# append to the hz file

wbRD = xlrd.open_workbook("{}/hz.xlsx".format(home))
sheets = wbRD.sheets()
wb = xlsxwriter.Workbook("{}/hz.xlsx".format(home))

for sheet in sheets:  # write data from old file
    newSheet = wb.add_worksheet(sheet.name)
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            newSheet.write(row, col, sheet.cell(row, col).value)
newSheet.write(0, 14, "distance from 55344 in km")
for row in range(1, len(distList)):  # write NEW data
    # for col in range(20):
    newSheet.write(row, 14, distList[row-1])
wb.close()  # THIS writes
print("done writing")
