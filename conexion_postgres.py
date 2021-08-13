import psycopg2 as pg
import json
def conectar():
    with open('./datos.json') as json_file:
        data = json.load(json_file)
    miConexion = pg.connect(host=data['host'], user = data['user'], password = data['passwd'], database = data['db'])
    return miConexion
