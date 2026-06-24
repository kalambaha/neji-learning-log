    #задача1
def calculate_bonus(a:int,b: float=10) -> float:
 return  a*(b/100)

print (calculate_bonus(5,25))

    #задача2
def show_shift_report(**kwargs) -> None:
 for key, value in kwargs.items(): 
  print(f"{key}: {value}")

show_shift_report(feet=42, eyes="blue", name="Anna")


    #задача3
def total_hours(*args) ->int:
 return sum(args)

print (total_hours(5,6,33,63))