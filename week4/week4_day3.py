def calculate_bonus(revenue: int, percent: float = 10) -> float:
    """
    Считает бонус чатера от выручки.

    Args:
        revenue: выручка за смену
        percent: процент бонуса (по умолчанию 10%)

    Returns:
        сумма бонуса
    """
    return revenue * (percent / 100)





def calculate_team_bonus(chaters: list[str], revenues: list[int], percent: float = 10) -> None:
    for number in range(len(chaters)):
         bonus = calculate_bonus(revenues[number])
         print(f"{chaters[number]} : {bonus}")






calculate_team_bonus(["Anna", "Kate", "Lisa"], [500, 300, 700])