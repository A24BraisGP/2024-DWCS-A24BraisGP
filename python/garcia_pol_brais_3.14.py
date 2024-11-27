products = {0: 'potatoes', 1:'tomatoes',3:'onions',4:'garlic'}

def show_dictionary(dictionary):
  for key, product in dictionary.items(): 
    text = f'The product number {key} is {product}'
    print(text)
    print('---------------')
    
show_dictionary(products)

products[2] = 'apples'
products[7] = 'lemon'

show_dictionary(products)

def find_value(dictionary, key):
  if key in dictionary.keys():
    item = dictionary[key]
    print('The item with the key ' + str(key) + ' is: ' + item)
  else: 
    print("There's no item with such key")
  
search_key = int(input('Which item do you need: '))
find_value(products,search_key)

product2 = {5:'lettuce',6:'carrots'}

#Outra opción é recorrer o segundo diccionario e en cada iteración engadilo sobre o primeiro
#Ordeei o diccionario para ver como se facía
def merge_dictionaries(dict1, dict2):
  merged_dict = {}
  for key, item in dict1.items():
    merged_dict[key] = item
  for key,item in dict2.items():
    merged_dict[key] = item
  print(f'Unsorted merged dictionary: {merged_dict}')
  sorted_dict = dict(sorted(merged_dict.items()))
  print(f'Sorted merged dictionary: {sorted_dict}')
  return sorted_dict  

merge_dictionaries(products,product2)


