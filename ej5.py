# -*- coding: utf-8 -*-
import json
with open ('hoteles.json') as data_file:
    data=json.load(data_file)
cod=(raw_input("Introduce el nombre del hotel: "))

for hoteles in data["resources"]:
    if hoteles["dc:identifier"]==cod:
        print hoteles["dc:title"]
        print hoteles["dc:description"]
        print "Localizacion: lat ",hoteles["geo:lat"]," y log ",hoteles["geo:long"]