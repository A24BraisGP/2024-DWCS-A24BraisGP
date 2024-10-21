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
