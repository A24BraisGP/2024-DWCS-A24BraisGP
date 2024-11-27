import json

# This function access the dictionary by the key, as we are familiar with the json structure that we are working with, we know we have to search in catalog, then book and then find the item with the given ID. 
def find_value(dictionary, book_id):
  book = dictionary['catalog']['book'][book_id-1]
  return book
  
#Via the with function it automatically does the try, except and finally close the file we are trying to open. As such, we access the file json and import it into a dictionary with the load() function (would've loads() in case of a json string). After that, we are free to treat it as a normal python dictionary, accessing its values with for ins. Nonetheless, we have to take in account the fact that is a nested dicionary, that is, in the values of some tuples there are other tuples with key value relationships
with open('python/catalog.json') as catalog_json:
  catalog_dict = json.load(catalog_json)
  for book in catalog_dict['catalog']['book']:
    for key,value in book.items():
      print(f'{key }  :  {value}')
      if key == 'description':
        print('-----------')

  for book in catalog_dict['catalog']['book']:
    for key,value in book.items():
      if key == 'title':
        print(f'The title is "{value}"')
        print('----------')
        
  for key, value in find_value(catalog_dict, 3).items():
    print(f'{key} : {value}')
