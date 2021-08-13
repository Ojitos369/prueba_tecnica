import pymysql
import json
def conectar():
    with open('./datos.json') as json_file:
        data = json.load(json_file)
    miConexion = pymysql.connect(host=data['host'], user = data['user'], passwd = data['passwd'], db = data['db'])
    return miConexion
