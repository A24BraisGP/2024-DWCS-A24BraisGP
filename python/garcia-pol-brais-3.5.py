def tripleCheck(arrayNum):
    count = 0
    check = False
    anterior  = None
    for item in arrayNum:
        if item== anterior:
            count += 1
        else: 
            count = 0
        if count == 2:
            check = True
            break
        anterior = item
    
    return check   
    

def countries(listCountries):
    for country, capital in listCountries.items():
        print(f"The capital of {country} is : {capital}")


print("Tripe check: ")
print(tripleCheck([1, 1, 2, 2, 1]))
print(tripleCheck([ 1, 1, 2, 1, 2, 3 ]))
print(tripleCheck([ 1, 1, 1, 2, 2, 2, 1]))
print(tripleCheck([1,2,2,1,3,5,5,5,4]))
print(tripleCheck([1,2,2,1,3,5,5,4]))

print("\nCountry List: ")
countryList = {"Italy":"Rome","Belgium":"Brussels", "Denmark":"Copenhagen","Finland":"Helsinki","Ireland":"Dublin"}
countryList2 = {"Spain":"Madrid", "Galicia":"Santiago de Compostela"}
countries(countryList)
countries(countryList2)


    

