#!/usr/bin/env python

from urllib.request import urlretrieve
import pandas as pd


files=[
"TYP_ROH_A-G.xlsx",
"TYP_ROH_H-M.xlsx",
"TYP_ROH_N-R.xlsx",
"TYP_ROH_S-V.xlsx",
"TYP_ROH_W-Z.xlsx"
]

first=True

for file in files:
    url=f"https://opendata.astra.admin.ch/ivzod/1000-Fahrzeuge_IVZ/1300-Fahrzeugbestaende/1330-Bestaende_nach_Typen/1333-Datensaetze/{file}"
    urlretrieve(url,file)
    xl = pd.ExcelFile(file)
    sheet_count=len(xl.sheet_names)
    for sheet_number in range(1,sheet_count): #omit the first sheet as it contains explanations
        data = pd.read_excel(file,sheet_name=int(sheet_number))
        data.to_csv('swiss-car-types.csv',header=first, mode='a' if not first else 'w')
        data.to_json('swiss-car-types.json',mode='a' if not first else 'w', orient="records",lines=True)
        first=False #after first sheet we only want to appen the data
