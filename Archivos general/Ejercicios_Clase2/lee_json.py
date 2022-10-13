import json
mi_json = open("datos.json","r", encoding = "UTF-8")
print(mi_json)

#al realizar la ejecución del archivo .py, da error, eso debido a la dirección del archivo
#eso debe ser corregido cambiando el directorio abriendo un nuevo terminal y agregando cd “Archivos general\Ejercicios_Clase2” para este caso y
# posteriormente, el comando python.exe lee_json.py

json_datos = mi_json.read()
datos = json.loads(json_datos)
print("json_datos:", json_datos)
print("datos:", datos)
print("temperaturas: ", datos["temperaturas"])
