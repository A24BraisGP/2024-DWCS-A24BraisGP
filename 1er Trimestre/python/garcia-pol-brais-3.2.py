'''In python the None keyword is used to define a null value, or no value at all.

Write a function that receives:

- A string, name, that can be null

- A string, surname, optional, default value "Apelido"

- An int, age.

It doesn't return anything.

The function shows a string on the screen showing:

   Nome Apelido is xx years old.'''
   
def nameShowing(age, name = None, surname = "Apelido"):
    if name is None:
        print("O nome ta nulo")        
    print(f"{name} {surname} is {age} years old")    

nameShowing(12,"Mateo","García")
nameShowing(12,"Mateo")
nameShowing(12,None)

