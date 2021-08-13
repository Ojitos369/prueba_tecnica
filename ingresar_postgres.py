import pandas as pd
import numpy as np
from conexion_postgres import conectar

def cargar():
    df = pd.read_csv('./datos.csv', sep = ',', header = 0)
    return df

def agregar_company(df):
    # Revisar los id unicos de las compañias
    companies = df['company_id'].unique()
    con = conectar()
    conexion = con.cursor()
    
    for i in range(len(companies)):
        # Obtener el primer indice que coincida con el id de la compañia para obtener el nombre
        indice = np.where(df['company_id'] == companies[i])[0][0]
        comp_id = df.iloc[indice]['company_id']
        comp_name = df.iloc[indice]['company_name']
        # Agregar cada id y nombre de las compañias a la base de datos
        query = f"INSERT INTO companies (id, name) VALUES ('{comp_id}', '{comp_name}');"
        print(query)
        conexion.execute(query)
    query = "SELECT * FROM companies"
    conexion.execute(query)
    con.commit()
    con.close()

def agregar_status(df):
    # Obtener los estados unicos
    status = df['status'].unique().tolist()
    con = conectar()
    conexion = con.cursor()

    for i in range(len(status)):
        # Obtener el primer indice que coincida con el estado para obtener el nombre
        indice = np.where(df['status'] == status[i])[0][0]
        stat = df.iloc[indice]['status']
        # Agregar cada id y nombre de los estados a la base de datos
        query = f"INSERT INTO status (id, state) VALUES ({i + 1}, '{stat}');"
        print(query)
        conexion.execute(query)
    query = "SELECT * FROM status"
    conexion.execute(query)
    con.commit()
    con.close()

def agregar_datos(df):
    con = conectar()
    conexion = con.cursor()
    for dato in df.values:
        # Obtener los valores requeridos del dataframe para agregar a la base de datos
        id = dato[0]
        company_id = dato[2]
        amount = dato[3]
        # Obtener el id del estado que corresponde con el nombre del estado
        query = f"SELECT id FROM status WHERE state='{dato[4]}';"
        conexion.execute(query)
        status_id = conexion.fetchone()[0]
        created_at = dato[5]
        # Si la updated_at no es valida se deja como null, en caso de ser valida se agrega a la base de datos
        if dato[6] == '0000-00-00 00:00:00':
            query = f"INSERT INTO charges (id, company_id, amount, status_id, created_at) VALUES ('{id}', '{company_id}', {amount}, {status_id}, '{created_at}');"
        else:
            updated_at = dato[6]
            query = f"INSERT INTO charges (id, company_id, amount, status_id, created_at, updated_at) VALUES ('{id}', '{company_id}', {amount}, {status_id}, '{created_at}', '{updated_at}');"
        print(query)
        conexion.execute(query)
    query = "SELECT * FROM charges"
    conexion.execute(query)
    con.commit()
    con.close()

def main():
    df = cargar()
    agregar_company(df)
    agregar_status(df)
    agregar_datos(df)


if __name__ == '__main__':
    main()