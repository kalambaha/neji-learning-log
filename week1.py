name = input("имя?")
sold = int(input("продаж?"))
time = int(input("time?"))
error = int(input("errors?"))
if sold>=15 and time <=5 and error==0:
    print (f"{name}- status TOP")
elif sold>=10 and time <=10 and error <= 1:
    print (f"{name}- status GOOD")
elif sold>=5 and error <= 3:
    print (f"{name}- status NORMA")
else:
    print(f"{name}- status Trouble")
