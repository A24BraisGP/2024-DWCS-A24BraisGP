##Crear un diccionario desde dúas listas separadas. 
words = ["List", "Dictionary", "Array"]

definitions = ["Ordered array of objects", "Unordered array of key-value pairs", "Mathematic definition"]
coolDictionary={}
## Creando o diccionario cun bucle
for num in range(0,len(words)):
  coolDictionary[words[num]]=definitions[num]


##Bucle for recorrendo o diccionario
print(f"The contents are:")
for element in coolDictionary:
  print(f"{element} : {coolDictionary[element]}")
  