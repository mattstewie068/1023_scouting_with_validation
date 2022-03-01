
raw_data = 's=gd;e=2022flwp;l=qm;m=29;r=b3;t=1023;as=[28];at=N;au=2;al=0;ac=Y;tu=5;tl=1;tm=3;tn=1;wd=N;cl=t;ss=[8];c=3;be=Y;cn=1;ds=a;dr=a;d=N;to=N;cf=N;co='

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