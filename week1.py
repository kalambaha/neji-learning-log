name = input("имя?")
hours = int(input("сколько часов?"))
perhour = int(input("ставка?"))
if hours <= 8:
    print(f"зарплата {name} : {hours * perhour}")
elif hours >8:
    print (f"зарплата  {name}:  {(hours - 8) * perhour * 1.5 + (8 * perhour)}")
