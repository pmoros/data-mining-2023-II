import json

with open('datasets/raw/eval_route_data_formatted.json',"r") as eval_route:
    data_eval_route = json.load(eval_route)

def obtener_todas_las_claves(objeto_json, prefijo=""):
    claves = []
    if isinstance(objeto_json, dict):
        for clave, valor in objeto_json.items():
            claves.append(clave)
    return claves
claves=obtener_todas_las_claves(data_eval_route)
claves = list(set(claves))


list_stops=[]
for clave in claves:
    for st in data_eval_route[clave]["stops"]:
        if st not in list_stops:
            list_stops.append(st)

processed = dict([])
for clave in claves:
    toADD = data_eval_route[clave]
    toADD['RouteID'] = str(clave).replace("RouteID_","")
    for stop in list_stops:
        if stop in toADD["stops"]:
            toADD[stop] = "1" if toADD["stops"][stop]['type'] == 'Dropoff' else "2"
        else:
            toADD[stop] = "0"
    del toADD['stops']
    processed[str(len(processed))] = toADD

with open('datasets/processed/eval_route_data_formatted.json', 'w') as file:
    json.dump(processed, file, indent=4)