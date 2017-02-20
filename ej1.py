# -*- coding: utf-8 -*-
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
