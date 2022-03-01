import pandas as pd

raw_data = 's=gd;e=2022flwp;l=qm;m=14;r=b2;t=4567;as=[44];at=Y;au=1;al=0;ac=N;tu=0;tl=0;tm=1;tn=0;wd=N;ss=[44,57];c=f;be=Y;cn=0;dr=v;d=Y;to=N;cf=Y;co=matt is awesome'

excel_file = 'scouting_data.xlsx'
df = pd.read_excel(excel_file)

print(" ")
print(raw_data)
print(" ")

headers = []
headerless_data = []

semicolon_split_scan = raw_data.split(";")

print(semicolon_split_scan)
print(" ")    

for x in range(len(semicolon_split_scan)):
    item = semicolon_split_scan[x]
    item = item.split("=")
    value = item[0]
    headers.append(value)
    value = item[1]
    headerless_data.append(value)

print(headers)
print(" ")
print(headerless_data)
print(" ")

data_dictionary = dict(zip(headers,headerless_data))

print(data_dictionary)

df = df.append(data_dictionary, ignore_index=True)
df.to_excel(excel_file, index=False)