# coding: utf-8
#!/usr/bin/env python
import pandas as pd

# Proveedores Fields: Ejercicio 	Nombre de la persona física/ Razón social	Nombre del representante de la empresa	Direccion	Colonia	Delegacion	Codigo Postal	Direccion electronica de la pagina WEB	Telefono oficial 	Correo electronico


toclean = pd.read_csv('proveedores.csv')
deduped = toclean.drop_duplicates(subset='Nombre de la persona física/ Razón social',take_last=True)
deduped.to_csv('proveedores_clean.csv')
