# -*- coding: utf-8 -*-
#Introducir las estrellas y mostrar los hoteles

import json
with open ('hoteles.json') as data_file:
    data=json.load(data_file)

estrellas=int(raw_input("Busqueda de hoteles por estrellas: "))

if estrellas>0 and estrellas<6:
    for hoteles in data["resources"]:
        if hoteles["dc:title"].count("*")==estrellas:
            print hoteles["dc:title"]
        elif hoteles["dc:title"].count("*")==estrellas:
            print hoteles["dc:title"]
        elif hoteles["dc:title"].count("*")==estrellas:
            print hoteles["dc:title"]
        elif hoteles["dc:title"].count("*")==estrellas:
            print hoteles["dc:title"]
        elif hoteles["dc:title"].count("*")==estrellas:
            print hoteles["dc:title"]
else:
    print "Error, introduce las estrellas del 1 al 5"