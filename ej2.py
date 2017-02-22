# -*- coding: utf-8 -*-
#Lista la cantidad de Hoteles clasificados por estrellas

import json
with open ('hoteles.json') as data_file:
    data=json.load(data_file)
e1=0
e2=0
e3=0
e4=0
e5=0
for hoteles in data["resources"]:
    if hoteles["dc:title"].count("*")==5:
        e5=e5+1
    elif hoteles["dc:title"].count("*")==4:
        e4=e4+1
    elif hoteles["dc:title"].count("*")==3:
        e3=e3+1
    elif hoteles["dc:title"].count("*")==2:
        e2=e2+1
    elif hoteles["dc:title"].count("*")==1:
        e1=e1+1


print "Hay",e5,"Hoteles de 5 estrellas"
print "Hay",e4,"Hoteles de 4 estrellas"
print "Hay",e3,"Hoteles de 3 estrellas"
print "Hay",e2,"Hoteles de 2 estrellas"
print "Hay",e1,"Hoteles de 1 estrella"
