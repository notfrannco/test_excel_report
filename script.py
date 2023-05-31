#!/bin/python

import pandas as pd
import csv
import pathlib

# abrir el csv de servidores creado con ansible para hacer un filtro extra usando la columna que
# representa el entorno, en este caso 'prod' y crear un nuevo cvs para una hoja de excel aparte
with open('servidores.csv', 'r') as f_in:
    with open('servidores_prod.csv', 'w') as f_outfile:
        f_out = csv.writer(f_outfile, delimiter='x') 
        for line in f_in:
            line = line.strip()
            row = []
            if 'prod' in line:
                row.append(line) 
                f_out.writerow(row)


# lista de csv que se dispone para leer
csv_files = ['servidores.csv', 'servidores_prod.csv']


# creacion de un excel con el reporte final 
with pd.ExcelWriter('reporte.xlsx') as writer:
    df = pd.read_csv(csv_files[0], names=['Servers', 'ip', 'hostname', 'entorno'])
    df.to_excel(writer, sheet_name='SERVERS', index=None)
    
    df = pd.read_csv(csv_files[1], names=['Servers', 'ip', 'hostname', 'entorno'])
    df.to_excel(writer, sheet_name='PRODUCCION', index=None)
