# -*- coding: utf-8 -*-
#Lista los hoteles por precio ("Alto","Medio","Economico")

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

print "Hoteles con precio ECONOMICO"
for ec in economico:
    print ec

print "Hoteles con precio MEDIO"
for me in medio:
    print me

print "Hoteles con precio ALTO"
for al in alto:
    print al

