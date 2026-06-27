# Задача 1
def my_list(numbers:list) -> None:
    """
    сортируем лист на четные и нечетные

   args:
    делить каждое значение на 2 что бы проверить четное число или нет
   returns:

   выдает 2а списка четных и не четных значений числами
    """
    for value in (numbers):
     if value % 2 == 0:
         print(f"{value} - четное")
     else:
         print(f"{value} - не четное")
my_list([3, 7, 1, 9, 4, 6, 2])

# Задача 2
def my_list1(compre:list)->list:
 """
создает новй список со словам где больше 4 букв из старого списка

args:
 проверяет длинну аргументов на то больше ли она 4 значениям или нет

 returns:
возвращет новый список слов с 4 значениями и более
 """
 newList = [words for words in compre if len(words)>=4]
 print(newList)

my_list1(["python", "code", "ai", "agent", "data"])

# Задача 3
def archive(her:list)->None:
 """
сортирует значения по их аргументу

args:
 подставляет к значению заданные слова и сортирует
returns:
возвращает список элементов  от 0 до последнего с заданной структурой
"""
 for number in range(len(her)):
  print (f"Element N:{number} - {her[number]}")

archive([3, 7, 1, 9, 4, 6, 2])