revenue = [1, 11, 22, 33, 44, 55, 66]
first_5 = revenue [:5]
last_2 = revenue [-2:]
for i, value in enumerate(revenue, 1):
    print(f"день:{i}-{value}")
    if value == min(revenue):
        worst_day = i
        worst_value = value
print(f" самый низкий показатель в день:{worst_day} {worst_value}")
