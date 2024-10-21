age = 45
name = "Julie"
# comentario
print("hello " + name)

sentence =f"Hello my name is {name} and i'm {age}"

print(sentence)

print("Hello my name is {} and i'm {}".format(name, age))

check = age > 18
#If else statement
if check:
  print("You're old")
elif age < 18:
  print("you're younger")

#one line comment 

"""Multiple
line
comment"""

year = 2050


if (year >= 2000 and year <= 2099):
  print(f"{year} is in the XXI century")
else:
  print(f"{year} is NOT in the XXI century")


#Otra manera de hacer python
  
print(f"{year} is in the XXI century") if (year >= 2000 and year <= 2099) else print(f"{year} is NOT in the XXI century")

#functions NON teñen hoisting. 

def hello(name_hello):
  print(f"Hello {name_hello}")
  
hello("Nick")
hello(name)

## Lista
dogname = ["fido","sean","sally","mark"]
print(dogname)

## Insertamos na posición un valor, sen sobreescribir
dogname.insert(1,"jane")
print(dogname)

## Sobreescribimos a posición 2 da lista
dogname[2] = "Peter"
print(dogname)

 ## Borramos a posición 2 da lista
del(dogname[2])
print(dogname)

## Imprimimos o número de elementos na lista
print(f'The number of elements in the list is {len(dogname)}')

##Loops 
##for in example
for dog in dogname:
  print(dog)
  
##For in with a range, creates a list with range  
cadea = ""  
for numero in range(1,10):
  cadea = cadea + str(numero) + " "
  
print(cadea)

##while loop 
num = 20
while(num > 18): 
  print(num)
  num= num -1
  
## Diccionarios, mapas clave:valor
dogs = {"Fido":8,"Sally":17,"Sean":2}
print(dogs)
##Usamola key para acceder ao valor
print(dogs["Sean"])
##Para engadir elementos podemolo facer a pelo cunha nova clave
dogs["Mark"] = 9
print(dogs)
##Para borrar
del(dogs["Fido"])
print(dogs)

##Crear un diccionario desde dúas listas separadas. 
words=["PoGo","Spange",False]
definitions=["Slang for Pokemon GO", "To collect spare change",True]
coolDictionary={}
## Creando o diccionario cun bucle
for num in range(0,len(words)):
  coolDictionary[words[num]]=definitions[num]


##Bucle for recorrendo o diccionario
print(f"The contents are:")
for element in coolDictionary:
  print(f"{element} : {coolDictionary[element]}")
  
##Clases
class Dog:
  
  def __init__(self, name, age, furcolor):
    self.name = name
    self.age = age
    self.furcolor = furcolor
  
  dogInfo = "Dogs are cool"
  
  def bark(self, str):
    print("Guau guau " + str)
    
    
## Declaración dunha variable como instancia dunha clase
myDog = Dog("Mark",27,"Brown")
print(myDog.furcolor)
print(myDog.name)
print(myDog.age)

## Para chamar a métodos temos que por self como primeiro parámetro
myDog.bark("Brais")
## Podemos incluir novas propiedades á instancia fora da clase
myDog.name="Fido"
myDog.age="16"
print(myDog.name)
print(myDog.age)
print(myDog.dogInfo)

