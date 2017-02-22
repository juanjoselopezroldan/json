# -*- coding: utf-8 -*-
#Introduce los dos ultimos numeros de un hotel y que muestre el nombre del hotel, la localizacion y una descripcion del mismo

import json
with open ('hoteles.json') as data_file:
    data=json.load(data_file)

tel=raw_input("Introduce los dos ultimos digitos del numero: ")

no="false"

for hoteles in data["resources"]:
    if hoteles["lpgc:telefono"][-2:]==tel:
        print hoteles["dc:title"]
        print hoteles["dc:description"]
        print "Localizacion: lat ",hoteles["geo:lat"]," y log ",hoteles["geo:long"]
        no="true"
if no=="false":
        print "Error, hotel no encontrado"
