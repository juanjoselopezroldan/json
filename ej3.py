# -*- coding: utf-8 -*-
import json
with open ('hoteles.json') as data_file:
    data=json.load(data_file)

estrellas=int(raw_input("Busqueda de hoteles por estrellas: "))