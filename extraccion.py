from conexion_mysql import conectar
import pandas as pd

def exportar(df, tipo):
    if tipo == 'csv':
        df.to_csv('datos.csv', index = False)
    elif tipo == 'xlsx':
        df.to_excel('datos.xlsx', index = False)
    else:
        print('Error de tipo, eliga entre "csv" o "xlsx"')

def imprimir():
    def comprobar(dato, agregar):
        # Comprueba si el dato no es NULL
        if agregar:
            if len(str(dato)) < 1:
                agregar = False
        return agregar
    
    conexion = conectar().cursor()
    conexion.execute("SELECT * FROM datos")
    datos_limpios = []
    datos = conexion.fetchall()

    # Quitamos los datos que no cumplan con la condicion en los campos NOT NULL
    i = 0;
    for dato in datos:
        agregar = True

        # Indices de los campos con condicion NOT NULL
        no_nulos = [0, 2, 3, 4, 5]
        for j in no_nulos: agregar = comprobar(dato[j], agregar)

        # Revisas que los Decimales no excedan los tamaños establecidos
        try:
            dato3 = float(dato[3])
            if len(str(round(dato3, 2))) > 18: agregar = False
        except:
            agregar = False
        
        # Si el dato actual cumple con los campos requeridos en NOT NULL es agregado
        if agregar:
            datos_limpios.append([])
            for elemento in dato:
                if elemento == dato[3]:
                    datos_limpios[i].append(round(float(elemento), 2))
                else:
                    datos_limpios[i].append(elemento)
            i += 1

    columnas = [
        'id',
        'company_name',
        'company_id',
        'amount',
        'status',
        'created_at',
        'updated_at'
    ]
    df = pd.DataFrame(datos_limpios, columns = columnas)
    print(df)
    tipo = input('Escriba el tipo para exportar los datos ("csv" / "xlsx": ')
    exportar(df, tipo)


if __name__ == "__main__":
    imprimir()