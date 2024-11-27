import json

def find_value(dictionary, book_id):
  book = dictionary['catalog']['book'][book_id-1]
  return book
  

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
