with open('recipes.txt', 'r', encoding = 'utf-8') as f:
    file = f.read() 
    
#print(file)

file_dishes = file.split("\n\n")
print(file_dishes)                       
cook_book = []
for dishes in file_dishes:
    


