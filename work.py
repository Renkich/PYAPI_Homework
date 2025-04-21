# Задание 1

import re

with open('recipes.txt', 'r', encoding = 'utf-8') as f:
    file = f.read() 

file_dishes = file.split("\n\n")                     
cook_book = {}
dishes = []
for items in file_dishes:
    parts = re.split(r'[\n|]+', items)
    dishes.append(parts[0])

name_ingridients = ['ingredient_name', 'quantity', 'measure']
ingridients = []
for items in file_dishes:
    parts = re.split(r'[\n]+', items)
    del parts[:2]
    ingridients.append(parts)

ingridients_all = []
for v in ingridients:
    b = [n.split(',') for n in v]
    ingr_parts = []  
    for d in b:             
        for n in d:
            c = [n.split('|') for n in d]
            f = c[0]
            #print(f)
            for l in f:              
                ingr = {}
                for h, l in zip(name_ingridients, f):                   
                    ingr[h] = l
                    
        #print(ingr)
        ingr_parts.append(ingr) 
    ingridients_all.append(ingr_parts)

#print(ingridients_all)
for dish, ingrid in zip(dishes, ingridients_all):
    cook_book[dish] = ingrid

for item in cook_book.items():
    print(item)

# Задание №2

def get_shop_list_by_dishes(dishes, person_count):
    ingr_pers = dict()
    for dish in dishes:
        if dish in cook_book:            
            for ingrid in cook_book[dish]:
                meas = dict()
                meas['measure'] = ingrid['measure']
                meas['quantity'] = int(ingrid['quantity'])*person_count
                ingr_pers[str(ingrid['ingredient_name'])] = meas
        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_pers            

print(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 5))

# Задание 3





    #ingridients = []
    #for i in items.split("|"):
        #ingridients['ingredient_name'] = i
        #ingridients['quantity'] = i
        #ingridients['measure'] = i
    #value = ingridients
    #cook_book[key] = value

#print(cook_book)

#with open('recipes.txt', 'r', encoding = 'utf-8') as f:
    #file = f.read() 
    
#print(file)

#file_dishes = file.split("\n\n")
#print(file_dishes)                       
#cook_book = {}
#dishes = []
#for items in file_dishes:
    #k = items.split(r'[\n, | ]+')
    #print(k)
    #dishes.append(str(k[0]))
   
#print(dishes)   
    #ingridients = []
    #for i in items.split("|"):
        #ingridients['ingredient_name'] = i
        #ingridients['quantity'] = i
        #ingridients['measure'] = i
    #value = ingridients
    #cook_book[key] = value

#print(cook_book)
    
#data = \
#"+1 градус\n\
#+10 градусов"
#data = data.split('\n')
#print(data)
#dt = []
#for l in data:
    #dt.append(l.split()[0])
    #print(dt)

#def get_shop_list_by_dishes(dishes, person_count):
    #ingr_pers = dict()
    #for dish in dishes:
        #if dish in cook_book:
            #meas = {}
            #for ingrid in cook_book[dish]:
                #meas = dict()
                #meas['measure'] = ingrid['measure']
                #meas['quantity'] = ingrid['quantity']*person_count
                #ingr_pers[ingrid['ingredient_name']] = meas
        #else:
            #print(f'\n"Такого блюда нет в списке!"\n')
    #return ingr_pers      