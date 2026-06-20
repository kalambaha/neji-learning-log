chaters = [['alex', 233], ['alena', 123], ['lera', 555], ['xer', 346]]

mylist= sorted(chaters, key=lambda x: x[1])
first_3 =mylist[-3:]
for i, value in enumerate (first_3[::-1]):
    print(f"mesto {i+1} {value[0]} - {value[1]}")
