# -*- coding: utf-8 -*-
import json
with open ('hoteles.json') as data_file:
    data=json.load(data_file)
alto=[]
medio=[]
economico=[]
for hoteles in data["resources"]:
    if hoteles["lpgc:precio"]=="Economico":
        economico.append(hoteles["dc:title"])
    if hoteles["lpgc:precio"]=="medio" or hoteles["lpgc:precio"]=="Precio medio":
        medio.append(hoteles["dc:title"])
    if hoteles["lpgc:precio"]=="Alto" or hoteles["lpgc:precio"]=="alto":
        alto.append(hoteles["dc:title"])



