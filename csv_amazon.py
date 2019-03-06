import csv
import os
with open('enthography.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        product_name=row[0].strip()
        os.system('amazon2csv.py --keywords="%s" --maxproductnb=2 >> final.csv' % product_name)
        print(row[0].strip())
csvFile.close()
