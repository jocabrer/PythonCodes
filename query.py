import pyodbc
import io
import pandas as pd


direccion_servidor = 'PC01\SQLEXPRESS2016'
nombre_bd = 'TTB_BD_VRS_PRG_32_D'
nombre_usuario = 'sa'
password = 'pernitos'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    # OK! conexión exitosa

    cursor = conexion.cursor()
    cursor.execute("SELECT  * FROM curvas")
    datos = cursor.fetchall()
    newfile = open("db-data.txt","a+")
    
    ##data cddo datos/1/xdsp 'xdsp.csv'

    for row in datos:
        print("Id: ", row[0])
        print("Name: ", row[1])
        print("Email: ", row[2])
        print("Salary: ", row[3])
        print("\n")
    cursor.close()
    

except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)

finally:
    if conexion:
        conexion.close()
        print("The SQLSERVER connection is closed")