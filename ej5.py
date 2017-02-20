# -*- coding: utf-8 -*-
#Introduce un codigo de hotel y que muestre el nombre del hotel, la localizacion y una descripcion del mismo

import json
with open ('hoteles.json') as data_file:
    data=json.load(data_file)

cod=(raw_input("Introduce el nombre del hotel: "))


for hoteles in data["resources"]:
    if hoteles["dc:identifier"]==cod:
        print hoteles["dc:title"]
        print hoteles["dc:description"]
        print "Localizacion: lat ",hoteles["geo:lat"]," y log ",hoteles["geo:long"]
        exit()
if hoteles["dc:identifier"]!=cod:
        print "Error, codigo no encontrado"