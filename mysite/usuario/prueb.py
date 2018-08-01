from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)
db = client["servicios"]

collection = db["misservicios"]

def fill_col(collection):
    file = open("static/data/todosmisservicios.csv",'r', encoding='utf8')
    for i in file:
        fila = i.split(";")
        if len(fila) == 5:
            collection.insert_one(
                {
                    "nombre" : fila[0],
                    "agencia" : fila[1],
                    "provincia" : fila[2],
                    "fecha" : fila[3],
                    "total" : fila[4],
                }
            )

algo = collection.find({'fecha':{"$regex":"^2018-01"}})
for alg in algo:
    print(alg)
print("hoal")
