name = input("name?")
month = int(input("how many?"))
deal = int(input("deals?"))
erors = input("erors? yes no -")
if month>=6 and deal>=20 and erors != "yes":
    print ("допущен к важному аккаунту")
elif month>=3 and deal>=10:
    print ("допущен к стандартному аккаунту") 
else:
    print("требует дополнительного обучения")  