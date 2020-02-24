#imports
import pandas as pd
import numpy as np
import os
from datetime import datetime

def calcWeight(d1):
    return round(1-(diff_month_from_today(datetime.strptime(d1,"%Y-%m"))/36)*0.5, 3)

def diff_month_from_today(d1):
        return (datetime.now().year - d1.year) * 12 + datetime.now().month - d1.month

path = r'C:\Users\Hamza\Desktop\TeamProj\crimeData'
all_files=[]
for r,d,f in os.walk(path):
    for file in f:
        if '.csv' in file:
            all_files.append(os.path.join(r,file))
            
crimeDfs = (pd.read_csv(f) for f in all_files)

allcrimesDf = pd.concat(crimeDfs, ignore_index=True, sort=True)

allcrimesDf = allcrimesDf.dropna(subset=['Longitude','Latitude','Location'])

allcrimesDf = allcrimesDf[allcrimesDf['LSOA name'].str.contains('Kirklees')]

allcrimesDf = allcrimesDf.filter(['Month','Longitude','Latitude','Crime type'])

allcrimesDf['Weight'] = allcrimesDf['Month'].apply(lambda x: calcWeight(x))

allcrimesDf.to_csv('crime_data.csv',sep=',',index=False,encoding='utf-8')

