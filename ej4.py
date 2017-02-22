# -*- coding: utf-8 -*-
#Introducir el nombre del hotel y muestre su pagina web

import json
with open ('hoteles.json') as data_file:
    data=json.load(data_file)
nombre=raw_input("Introduce el nombre del hotel: ").upper()
no="false"
for hoteles in data["resources"]:
    if hoteles["dc:title"][+6:].upper()==nombre:
        if hoteles["lpgc:web"] == "":
            print "El hotel",hoteles["dc:title"]," no tiene url"
        else:
            print "El hotel",hoteles["dc:title"]," tiene la siguiente url: ",hoteles["lpgc:web"]
        no="true"
    if hoteles["dc:title"][+5:].upper()==nombre:
        if hoteles["lpgc:web"] == "":
            print "El hotel",hoteles["dc:title"]," no tiene url"
        elif hoteles["lpgc:web"] != "":
            print "El hotel",hoteles["dc:title"]," tiene la siguiente url: ",hoteles["lpgc:web"]
        no="true"
    if hoteles["dc:title"][+4:].upper()==nombre:
        if hoteles["lpgc:web"] == "":
            print "El hotel",hoteles["dc:title"]," no tiene url"
        elif hoteles["lpgc:web"] != "":
            print "El hotel",hoteles["dc:title"]," tiene la siguiente url: ",hoteles["lpgc:web"]
        no="true"
    if hoteles["dc:title"][+3:].upper()==nombre:
        if hoteles["lpgc:web"] == "":
            print "El hotel",hoteles["dc:title"]," no tiene url"
        elif hoteles["lpgc:web"] != "":
            print "El hotel",hoteles["dc:title"]," tiene la siguiente url: ",hoteles["lpgc:web"]
        no="true"
    if hoteles["dc:title"][+2:].upper()==nombre:
        if hoteles["lpgc:web"] == "":
            print "El hotel",hoteles["dc:title"]," no tiene url"
        elif hoteles["lpgc:web"] != "":
            print "El hotel",hoteles["dc:title"]," tiene la siguiente url: ",hoteles["lpgc:web"]
        no="true"

if no=="false":
    print "Hotel no encontrado"