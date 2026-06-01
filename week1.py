name = input("имя?")
sold = int(input("сколько продаж?"))
plan = int(input("план продаж?"))
if sold < plan:
    print("ПЛАН не выполнен!")
elif sold >= plan:
    print (f"План выполнен  {name}:  {(sold/plan)*100}" , "%")
