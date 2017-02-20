# -*- coding: utf-8 -*-
import json
with open ('hoteles.json') as data_file:
    data=json.load(data_file)
nombre=raw_input("Introduce el nombre del hotel: ").upper()