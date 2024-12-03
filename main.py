from random import randint 
indexminus = 0
indexplus = 0
indexnol = 0
num_max = 0
num_min = 0
num_list = [randint(-50, 50) for i in range(20)]#создает список из 30 символов от -50 до 50 
for i in num_list:
    if num_max < i:
        num_max = i
    if num_min > i:
        num_min = i
    if i < 0:
        indexminus += 1
    elif i > 0:
        indexplus += 1
    else:
        indexnol += 1
print("chisla - : ", indexminus)
print("chisla + : ", indexplus)
print("nuli : ", indexnol)
precent_min = indexplus / 20 * 100
precent_max = indexminus / 20 * 100
print("chisla - : ", precent_min, "%")
print("chisla + : ", precent_max, "%")
print("max chislo: ", num_max)
print("min chislo: ", num_min)
