
qr_code_scan = 's=gd;e=2022flwp;l=qm;m=14;r=b2;t=4567;as=[44];at=Y;au=1;al=0;ac=N;tu=0;tl=0;tm=1;tn=0;wd=N;ss=[44,57];c=f;be=Y;cn=0;dr=v;d=Y;to=N;cf=Y;co=matt is awesome'

#open text file
text_file = open("C:1023_scouting", "a")
 
#write string to file
text_file.write('\n')
text_file.write(qr_code_scan)
 
#close file
text_file.close()