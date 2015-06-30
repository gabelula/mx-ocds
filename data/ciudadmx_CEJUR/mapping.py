#!/usr/bin/env python
import argparse
import contextlib
import copy
import csv
import json
import urllib2
import urlparse
import uuid
from datetime import date

# Proveedores Fields: Ejercicio 	Nombre de la persona física/ Razón social	Nombre del representante de la empresa	Direccion	Colonia	Delegacion	Codigo Postal	Direccion electronica de la pagina WEB	Telefono oficial 	Correo electronico
def main():
    parser = argparse.ArgumentParser(
        description='Convert CSV files to the OpenContracting format using '
                    'a given mapping.')
    parser.add_argument('--csv-file', metavar='proveedores.csv', type=str,
                        required=True, help='the csv file to convert')
    parser.add_argument(
        '--mapping-file', metavar='proveedores.json', type=str, required=True,
        help='the mapping used to convert the csv file')

    options = parser.parse_args()

    result = process(
        options.csv_file, options.mapping_file)
    print(result.encode('utf-8'))


if __name__ == '__main__':
    main()
