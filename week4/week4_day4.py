def top_chater(names: list[str], revenues: list[int]) -> str:
    """находит чатера с максимальной выручкой и возвращает его имя

       Args:
        
       Returns:
       имя + выручка

    """
    max_revenue = revenues[0]
    max_name = names[0]
    for i in range(len(revenues)):
     if revenues[i] > max_revenue:
         max_revenue = revenues[i]
         max_name = names[i] 
    return max_name
    
print(top_chater(["Anna", "Kate", "Lisa"], [500, 300, 700]))
     