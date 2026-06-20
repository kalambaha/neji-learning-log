# Задача 1
list = [3, 7, 1, 9, 4, 6, 2]
for value in (list):
    if value % 2 == 0:
     print(f"{value} -четное")
    else:
     print(f"{value} - не четное")

# Задача 2
my_list = ["python", "code", "ai", "agent", "data"]
newList = [words for words in my_list if len(words)>=4]
print(newList)

# Задача 3
archive = [10, 25, 30, 45, 50]
for number in range(len(archive)):
    print (f"Element N:{number} - {archive[number]}")