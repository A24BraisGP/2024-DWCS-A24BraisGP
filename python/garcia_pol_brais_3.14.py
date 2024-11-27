products = {0: 'potatoes', 1:'tomatoes',3:'onions',4:'garlic'}

#In order to print the diccionary we iterate over their items via a desestructuration of their key and value (product in this case)

def show_dictionary(dictionary):
  for key, product in dictionary.items(): 
    text = f'The product number {key} is {product}'
    print(text)
    print('---------------')
    
show_dictionary(products)

products[2] = 'apples'
products[7] = 'lemon'

show_dictionary(products)

#We look if the list of keys in dictionary contains the specific one asked in input, if it does, we access it and print it, if it doesn't, we show the error and finish the function
def find_value(dictionary, key):
  if key in dictionary.keys():
    item = dictionary[key]
    print('The item with the key ' + str(key) + ' is: ' + item + "\n")
  else: 
    print("There's no item with such key")
  
search_key = int(input('Which item do you need: '))
find_value(products,search_key)

product2 = {5:'lettuce',6:'carrots'}

#Outra opción é recorrer o segundo diccionario e en cada iteración engadilo sobre o primeiro
#Ordeei o diccionario para ver como se facía
#This function creates a new dictionary with the items and keys of the two we currently have. We could merge only the items in case we think some key might be duplicated, or search for it and replace it, but in this case there is no need for that. Additionaly I sorted the dictionary in order to investigate and search how it's supposed to be done
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


